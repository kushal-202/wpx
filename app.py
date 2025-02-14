from flask import Flask, render_template_string, request, jsonify
from werkzeug.utils import secure_filename
import os
import time
from whatsapp_web import WhatsAppWebAPI

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

api = WhatsAppWebAPI()

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        content = f.read()
    return render_template_string(content)

@app.route('/pair', methods=['GET'])
def pair():
    result = api.pair()
    return jsonify(result)

@app.route('/qr', methods=['GET'])
def qr():
    qr_code = api.get_qr_code()
    return jsonify({"qr_code": qr_code})

@app.route('/gc', methods=['GET'])
def group_uid():
    groups = api.get_group_list()
    return jsonify({"groups": groups})

@app.route('/send', methods=['POST'])
def send_message():
    session_id = request.form['sessionId']
    target_number = request.form['targetNumber']
    time_delay = int(request.form['timeDelay'])
    target_type = request.form['targetType']
    sender_name = request.form['senderName']
    
    file = request.files['sms']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    with open(filepath, 'r') as f:
        messages = f.readlines()

    result = api.send_bulk_messages(session_id, target_number, messages, time_delay, target_type, sender_name)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

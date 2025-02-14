from flask import Flask, request, jsonify, render_template
from whatsapp_api_client import WhatsAppWeb
import time

app = Flask(__name__)
whatsapp = WhatsAppWeb()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pair', methods=['POST'])
def pair_device():
    phone_number = request.form.get('phone_number')
    session_id = whatsapp.pair_device(phone_number)
    if session_id:
        whatsapp.send_message(phone_number, f"Your session token: {session_id}")
        return jsonify({"session_id": session_id, "status": "success"})
    return jsonify({"status": "failed"})

@app.route('/qr')
def qr_login():
    qr_code = whatsapp.generate_qr_code()
    return render_template('qr.html', qr_code=qr_code)

@app.route('/groupuid')
def get_group_uids():
    group_uids = whatsapp.fetch_group_uids()
    return jsonify({"group_uids": group_uids})

if __name__ == '__main__':
    app.run(debug=True)

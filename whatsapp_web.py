from time import sleep
import json

class WhatsAppWebAPI:
    def __init__(self):
        self.session = None

    def pair(self):
        self.session = "new_session_token"
        return {"status": "success", "session_id": self.session}

    def get_qr_code(self):
        return "Generated QR Code Here"

    def get_group_list(self):
        return ["Group 1", "Group 2", "Group 3"]

    def send_bulk_messages(self, session_id, target, messages, delay, target_type, sender):
        if session_id != self.session:
            return {"error": "Invalid session"}
        
        for msg in messages:
            print(f"Sending '{msg.strip()}' to {target} via {target_type} from {sender}")
            sleep(delay)
        return {"status": "Messages sent successfully!"}

import json
from channels.generic.websocket import WebSocketConsumer


class ChatConsumer(WebSocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connecion_establised',
            'message': 'Hello World!',            
        }))
    def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('Message:', message)
    self.send(text_data=json.dumps({
        'type': 'message',
        'message': message,
    }))
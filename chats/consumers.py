import json
from channels.generic.websocket import WebSocketConsumer


class ChatConsumer(WebSocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connecion establised',
            'message': 'Hello World!',            
        }))
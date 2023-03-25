from channels.generic.websocket import WebsocketConsumer
""" Send message to reload to frontend """
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import json

id = None
class MyConsumer(WebsocketConsumer):
    
    def connect(self): 
        global id
        self.accept()
        id = self

        self.send(text_data=json.dumps({
            'message': 'Hello world'
        }))

        

    @receiver([post_save, post_delete])
    def my_handler(sender, **kwargs):
        global id
        if id:
            id.send(text_data=json.dumps({
                "message": "reload"
            }))

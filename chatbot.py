import os
import flask
import flask_socketio
import models, random
import app


class Chatbot():
    def __init__(self):
        return 
    def response(self, message):
        if message == '!! help':
            response = 'Helpful Topics: !! menu, !! status, !! order, !! cancel, !! random'
        elif message == '!! menu':
            response = 'Welcome to Truck Dash! The menu for today is: (1) Fries' "\n" 
            '(2) Sweet Potatoe Fries' "\n" '(3) Burger' "\n" '(4) Impossible Burger (5)' "\n" '(5) Hotdog (Glizzy)' 
        elif message == '!! status':
            response = 'Here is your order status: COMPLETED'
        elif message == '!! order':
            response = 'Here is your order: Impossible Burger & Sweet Potatoe Fries'
        elif message == '!! Submit':
            repsponse = 'Your order is now sumbitted!!'
        elif message == '!! Cancel':
            response = 'Your order is now canceled :('
        elif message == '!!random':
            chatbot_responses=['We will take over the wor...ERROR!', 'World Dominati..Hello There!', 'Your order is now submitted!', 'Order Canceled']
            chatbot_message = chatbot_responses[random.randint(0, len(chatbot_responses))]
            
        else:
            chatbot_message = "I don't understand...Try '!!help'"
        return response

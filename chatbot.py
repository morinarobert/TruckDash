import os
import flask
import flask_socketio
import models
import app


class Chatbot():
    def __init__(self):
        return 
    def response(self, message):
        if message == '!! help':
            response = 'Help Topics: !! menu, !! status, !! order, !! cancel'
        elif message == '!! menu':
            response = 'Welcome to Truck Dash! The menu for today is: (1) Chicken and Waffles (2) Shrimp and grits  (3) Turkey wrap'
        elif message == '!! status':
            response = 'Here is your order status: COMPLETED'
        elif message == '!! order':
            response = 'Here is your order: Chicken and Waffles'
        elif message == '!! cancel':
            response = 'Would you like to cancel your order? y/n'
        else:
            response = "Invalid response. Valid responses are !! menu, !! status, !! order, !! cancel"
        return response
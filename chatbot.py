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
            response = 'Helpful Topics: !! Begin, !! order, !! View Order Status, !! status, !! cancel'
        elif message == '!! Begin':
            response = 'Welcome to Truck Dash! Please Pick a Food Truck to order food from: (!! 1) District Barbecue' 
            '(!! 2) Korean BBQ Taco Box' "\n" '(!! 3) The Orange Cow' "\n" '(!! 4) District Barbecue' "\n" '(!! 5) Capital Chicken and Waffles'
        elif message == '!! a':
            response = 'You ordered the: Barbecue Chicken. Is your order completed? !! Y / !! N'
        elif message == '!! Y':
            response = 'Your order is now sumbitted! Your order will be ready in 30 seconds. To view the status of your order type: !! status'
        elif message == '!! 1':
            response = 'District Barbeque: ' 'PLEASE CHOOSE FOOD OPTIONS FROM THE MENU: (1) Barbecue Chicken (2) Sliced Brisket Plate (3) Smoked BBQ Potato'
        elif message == '!! 5':
            response = 'Capital Chicken and Waffles: ' 'PLEASE CHOOSE FOOD OPTIONS FROM THE MENU' "\n" "\n" 'Boat Combo' "\n" 'Meal Combo' 
            "\n" 'Chicken and Fries' "\n" 'Banana Pudding' "\n" 'Chicken Sandwich Meal' "\n" '.....'
        elif message == '!! status':
            response = 'Here is your order status: COMPLETED'
        elif message == '!! order':
            response = 'Here is your order: Barbeque Chicken -- DISTRICT BARBEQUE'
        elif message == '!! Submit':
            repsponse = 'Your order is now sumbitted!!'
        elif message == '!! Cancel':
            response = 'Your order is now canceled :('
        elif message == '!! View Order Status':
            chatbot_responses=['Placing order', 'Prepping Food', 'Food Ready for pickup!']
            chatbot_message = chatbot_responses[random.randint(0, len(chatbot_responses))]
            
        else:
            chatbot_message = "I don't understand...Try '!!help'"
        return response

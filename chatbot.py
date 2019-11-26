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
            response = 'Helpful Topics: !! Begin, !! status, !! order, !! cancel, !! random'
        elif message == '!! Begin':
            response = 'Welcome to Truck Dash! Please Pick a Food Truck to order food from:' "\n" '(1) Dangerously Delicious Pies' "\n" 
            '(2) Korean BBQ Taco Box' "\n" '(3) The Orange Cow' "\n" '(4) District Barbecue' "\n" '(5) Capital Chicken and Waffles'
        elif message == '1':
            response = 'Dangerously Delicious Pies: ' 'PLEASE CHOOSE FOOD OPTIONS FROM THE MENU' "\n" "\n" 'Banana Cream' "\n" 'Blueberry Pancake Pie (BPP)' 
            "\n" 'Baltimore Bomb' "\n" 'Elvis' "\n" 'Pecan' "\n" 'Apple Crump' "\n" '.....'
        elif message == '2':
            response = 'Korean BBQ Taco Box: ' 'PLEASE CHOOSE FOOD OPTIONS FROM THE MENU' "\n" "\n" 'Chicken Taco Box' "\n" 'Fried Cheese Roll'
            "\n" 'Chicken Teriyaki with Rice (CTR)' "\n" 'KFC with Rice' "\n" 'Beef Bulgogi Taco Box (BBTB)' "\n" '.....'
        elif message == '3':
            response = 'The Orange Cow: ' 'PLEASE CHOOSE FOOD OPTIONS FROM THE MENU' "\n" "\n" 'Ice Cream Sandwich' "\n" 'Frozen Banana on Stick'
            "\n" 'MilkShake' "\n" 'Smoothie' "\n" 'Italian Ice Cup' "\n" '.....'
        elif message == '4':
            response = 'District Barbeque: ' 'PLEASE CHOOSE FOOD OPTIONS FROM THE MENU' "\n" "\n" 'Barbecue Chicken' "\n" 'Sliced Brisket Plate'
            "\n" 'Smoked BBQ Potato' "\n" 'The Carolina' "\n" 'BarbeQulossal "The Q" (Signature)' "\n" '.....'
        elif message == '5':
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
            chatbot_responses=['No current order','Placing order', 'Prepping Food', 'Food Ready for pickup!', 'Food Delivered']
            chatbot_message = chatbot_responses[random.randint(0, len(chatbot_responses))]
            
        else:
            chatbot_message = "I don't understand...Try '!!help'"
        return response

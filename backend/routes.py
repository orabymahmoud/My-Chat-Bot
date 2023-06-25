from . import app
import os
import json
import pymongo
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401
from pymongo import MongoClient
from bson import json_util
from pymongo.errors import OperationFailure
from pymongo.results import InsertOneResult
from bson.objectid import ObjectId
import sys
from datetime import datetime

# Get the path of the subdirectory containing the chatterbot package
chatterbot_dir = os.path.join(os.path.dirname(__file__), 'chatterbot')

# Add the directory to Python's search path
sys.path.append(chatterbot_dir)
# Now you can import the bot_talk function from the chatterbot.bot module
from bot import Bot_Chat , Bot_Train , Bot_Train_Specific

def parse_json(data):
    return json.loads(json_util.dumps(data))

######################################################################
# INSERT CODE HERE
######################################################################

@app.route("/health")
def health():
    return {"status":"OK"}, 200



@app.route("/chatBot" , methods = ["POST"])
@cross_origin(origin='localhost:3000',headers=['Content- Type','Authorization'])
def bot_talk():
    data = request.get_json()
    if 'message' in data and data['message'] is not None:
        message = data['message'] 
        if message is not None:
            response = jsonify({
                "Response": str(Bot_Chat(message)) ,
                "Status": 'Success',
                "ResultCode": '0',
                "RowVersion": datetime.now()
             })
            response.headers.add('Access-Control-Allow-Origin', 'localhost:3000')
            return response, 200
        else:
            response = jsonify({
                "Response": 'The message is missing' ,
                "Status": 'Failed',
                "ResultCode": '1',
                "RowVersion": datetime.now()
             })
            response.headers.add('Access-Control-Allow-Origin', 'localhost:3000')
            return response, 300
    elif 'train_bot' in data and data['train_bot'] is not None:
        train_bot = data['train_bot']
        if train_bot == 'True':
            Bot_Train()
            response = jsonify({
                "Response": 'Bot have trained Succesfully',
                "Status": 'Success',
                "ResultCode": '0',
                "RowVersion": datetime.now()
                })
            response.headers.add('Access-Control-Allow-Origin', 'localhost:3000')
            return response, 200
        else:
            response = jsonify({
                "Response": 'Bot have not trained',
                "Status": 'Failed',
                "ResultCode": '1',
                "RowVersion": datetime.now()
                })
            response.headers.add('Access-Control-Allow-Origin', 'localhost:3000')
            return response, 300
    else:
        response = jsonify({
                "Response": 'Body is empty',
                "Status": 'Failed',
                "ResultCode": '1',
                "RowVersion": datetime.now()
                })
            response.headers.add('Access-Control-Allow-Origin', 'localhost:3000')
            return response, 300



@app.route("/TrainBot" , methods = ["POST"])
@cross_origin(origin='localhost:3000',headers=['Content- Type','Authorization'])
def bot_train():
    data = request.get_json()
    if 'message' in data and data['message'] is not None and 'response' in data and data['response'] is not None:
        message = data['message'] 
        response = data['response'] 
        if message is not None:
            Bot_Train_Specific(message , response)
            return jsonify({
                "Response": 'Bot have trained Succesfully',
                "Status": 'Success',
                "ResultCode": '0',
                "RowVersion": datetime.now()
                }), 200
        else:
            return jsonify({
                "Response": 'The message is missing',
                "Status": 'Failed',
                "ResultCode": '1',
                "RowVersion": datetime.now()}), 300
    
    else:
        return jsonify({
                "Response": 'Body is Invalid',
                "Status": 'Failed',
                "ResultCode": '1',
                "RowVersion": datetime.now()}), 300

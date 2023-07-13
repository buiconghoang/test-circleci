from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import json_util 
import os
from datetime import datetime



app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

mongodb_url = os.getenv('MONGODB_URL')
port = os.getenv("PORT")
host = os.getenv("HOST")
is_debug_mode = os.getenv("IS_DEBUG_MODE")

# Connect to MongoDB
client = MongoClient(mongodb_url)
db = client['todoapp']
collection = db['todos']

@app.route('/')
def index():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Hello world ", current_time)
    return render_template('index.html')


@app.route('/get-list')
def get_list():
    # Retrieve all to-do documents
    todos = collection.find()
    todos_list = list(todos)
    return  json_util.dumps(todos_list )

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form['task']

    # Create a new to-do document
    todo = {'task': task, 'done': False}

    # Insert the document into the collection
    collection.insert_one(todo)
    return redirect('/')

@app.route('/done', methods=['POST'])
def mark_todo_done():
    task = request.form['task']

    # Find the to-do document
    todo = collection.find_one({'task': task})

    if todo:
        # Update the 'done' field to True
        collection.update_one({'_id': todo['_id']}, {'$set': {'done': True}})

    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_todo():
    task = request.form['task']

    # Delete the to-do document
    collection.delete_one({'task': task})

    return redirect('/')

if __name__ == '__main__':
    print("locahost: ", host)
    print("port: ", port)
    print("mongodb url: ", mongodb_url)
    app.run(host=host, port=port, debug=is_debug_mode)

# Close the MongoDB connection
client.close()

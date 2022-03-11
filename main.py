from flask import request
from flask import Flask
from flask import jsonify
import requests
import json
# from flask_sslify import SSLify

from sqliter import SQLighter
from message_parser import message_checker
from bot import write_json
from bot import send_message
# https://api.telegram.org/bot1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg/setWebhook?url=https://98919559b2dd27.lhrtunnel.link


#СОЗДАНИЕ СЕРВЕРА
app = Flask(__name__)
# sslify = SSLify(app)


TOKEN = '1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg'
URL = f'https://api.telegram.org/bot{TOKEN}/'
db = SQLighter('db.db')

def write_json(data, file_name='answer.json'):#ЗАПИСЬ JSON
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_message(chat_id, text='simple_text'):
    url = URL + 'sendMessage'
    message = {'chat_id': chat_id, 'text':text}
    r = requests.post(url, json=message)
    return r.json()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        try:
            chat_id= r['message']['chat']['id']
            text = r['message']['text']
        except:
            chat_id = r['edited_message']['chat']['id']
            text = r['edited_message']['text']
        send_message(chat_id, text=message_checker(chat_id, text))
        write_json(r)
        return jsonify(r)
    return '<h1>Стартовая страница</h1>'

@app.route('/send_message', methods=['POST', 'GET'])
def send_global_message():
    if request.method == 'GET':
        text = request.args.get('text')
        user_id = db.return_users()
        print(user_id)
        send_message(668296537, text=text)
    return '<h1>GLOBAL_MESSAGE</h1>'


@app.route('/remove_user', methods=['POST', 'GET'])
def remove_user_from_db():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        print(db.add_subscriber(user_id))
    return '<h1>REMOVE USER</h1>'

@app.route('/add_user', methods=['POST', 'GET'])
def add_user_to_db():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        print(db.add_subscriber(user_id))
    return '<h1>AD USER</h1>'

if __name__ == "__main__":
    app.run()


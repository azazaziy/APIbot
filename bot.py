from sqliter import SQLighter
import requests
import json

# https://api.telegram.org/bot1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg/setWebhook?url=https://98919559b2dd27.lhrtunnel.link

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
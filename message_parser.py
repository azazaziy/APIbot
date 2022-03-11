from sqliter import SQLighter
from messages import  MESSAGES

db = SQLighter('db.db')

def message_checker(chat_id, text):
    if text == '/sub':
        if db.subscriber_exists(chat_id):
            if db.subscription_info(chat_id):
                return MESSAGES['already_sub']
            else:
                db.update_subscription(chat_id, True)
                return MESSAGES['sub']

        else:
            db.add_subscriber(chat_id)
            return MESSAGES['sub']
    elif text == '/unsub':
        db.update_subscription(chat_id, False)
        return MESSAGES['unsub']
    else:
        return text[::-1]


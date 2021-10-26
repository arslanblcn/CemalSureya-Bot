from datetime import datetime
from constants import * 

def responses(user_input):
    user_message = str(user_input).lower()
    create_poet = get_random_poet()
    create_poetry = get_random_poetry(create_poet)
    create_poem_lines = get_random_lines(create_poetry)
    if user_message in ['hello', 'hi', 'what\'s up', 'sup']:
        return "Welcome Dear!"
    if user_message in ['How are you?', 'how are you?', 'sup']:
        return "Hey! How's it going on?"
    if user_message in ['date', 'time']:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y - %H:%M:%S")
        return str(date_time)
    if user_message in ['poem', 'poet']:
        return create_poet + "\n" + create_poetry + "\n" + create_poem_lines
    return "Something went wrong!"
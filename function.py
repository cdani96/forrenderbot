import telegram
from flask import request

def handler(request):
    try:
        bot = telegram.Bot(token='5464846915:AAE1qlyt5AkJOGsNWJe6x_a9aRqS0QscSwo')

        if request.method == "POST":
            update = telegram.Update.de_json(request.get_json(force=True), bot)
            chat_id = update.message.chat.id
            message = update.message.text
            bot.send_message(chat_id=chat_id, text="You said: {}".format(message))

    except Exception as e:
        print(e)

    return "ok"

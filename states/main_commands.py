from telebot.handler_backends import State, StatesGroup
from loader import bot

# 1. lowprice
# 2. highprice
# 3. bestdeal
class UserRequest(StatesGroup):
    city = State()
    check_in_date = State()
    check_out_date = State()
    command = State()
    photo = State()
    count_photo = State()


    def get_command_bd(chat_id:int):
        text = "Choose command or write it down: \n/help\n/lowprice\n/highprice\n/bestdeal\n/history"
        list_commands = ''
        bot.send_message(chat_id, text)
        bot.send_message(chat_id, list_commands)



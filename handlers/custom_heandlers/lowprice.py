from telebot.types import Message
from loader import bot

@bot.message_handler(commands="lowprice")
def lowprice(message:Message):
    text = "Enter the number of hotels (a number from 1 to 5)"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, photo_request)

def photo_request(message:Message):
    text = "The need to upload and display photos for each hotel"
    # a = bot.
    reply_keyboard = [['Yes','No']]
    bot.send_message(message.chat.id, text, reply_markup=reply_keyboard)
    print(message.text)

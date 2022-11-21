from loader import bot
from states.main_commands import UserRequest
from telebot.types import Message
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP


@bot.message_handler(commands = "start")
def city(message: Message)->None:

    text = "Enter diraction(City): "
    bot.send_message(message.from_user.id, text)
    bot.set_state(message.from_user.id, UserRequest.city, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['city'] = message.text

    bot.set_state(message.from_user.id, UserRequest.check_in_date, message.chat.id)


# @bot.message_handler(state = UserRequest.city)
# def city_in(message:Message)-> None:

@bot.message_handler(state = UserRequest.check_in_date)
def check_in(message: Message)->None:
    text = "Chose Check In Date: "
    bot.send_message(message.chat.id, text)
    calendar, step = DetailedTelegramCalendar(calendar_id = 1).build()
    bot.send_message(message.from_user.id,
         f"Select {LSTEP[step]}",
         reply_markup=calendar)

@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id = 1))
def call(callback):
    result, key, step = DetailedTelegramCalendar(calendar_id=1).process(callback.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              callback.message.chat.id,
                              callback.message.message_id,
                              reply_markup=key)

    elif result:
        bot.edit_message_text(f"You selected {result}",
                              callback.message.chat.id,
                              callback.message.message_id)
        with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
            data['check_in_date'] = str(result)

        bot.set_state(callback.message.from_user.id, UserRequest.check_out_date, callback.message.chat.id)
        check_out(callback.message.chat.id)



def check_out(chat_id: int)->None:
    text = "Chose Check Out Date: "
    bot.send_message(chat_id, text)
    calendar, step = DetailedTelegramCalendar(calendar_id=2).build()
    bot.send_message(chat_id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)

@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id = 2))
def call(callback):
    result, key, step = DetailedTelegramCalendar(calendar_id=2).process(callback.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              callback.message.chat.id,
                              callback.message.message_id,
                              reply_markup=key)

    elif result:
        bot.edit_message_text(f"You selected {result}",
                              callback.message.chat.id,
                              callback.message.message_id)
        with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
            data['check_out_date'] = str(result)
        bot.set_state(callback.message.from_user.id, UserRequest.command, callback.message.chat.id)
        selection_next_step_mod(callback.message)

def selection_next_step_mod(message: Message):
    text = "Choose command or write it down: " \
           "\n/help" \
           "\n/lowprice" \
           "\n/highprice" \
           "\n/bestdeal" \
           "\n/history"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, selection_next_step)


def selection_next_step(message: Message):
    command = message.text
    print(command)
    if command == "/lowprice":
        bot.send_message(message.chat.id, "/sdf")
    elif command == "/highprice":
        bot.send_message(message.chat.id, '/high')
    el
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from states.main_commands import UserRequest
# from handlers.custom_heandlers.lowprice import checOutDate



#
# @bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id = 1))
# def call(callback):
#     result, key, step = DetailedTelegramCalendar().process(callback.data)
#     if not result and key:
#         bot.edit_message_text(f"Select {LSTEP[step]}",
#                               callback.message.chat.id,
#                               callback.message.message_id,
#                               reply_markup=key)
#         # print(c.data)
#         # print(type(c.data))
#     elif result:
#         bot.edit_message_text(f"You selected {result}",
#                               callback.message.chat.id,
#                               callback.message.message_id)
#         checOutDate(callback.message.chat.id)
#         # print(c.message.text)
        # print(f'statte message.from_user.id{callback.from_user.id}, message.chat.id {callback.message.chat.id} ')
        # bot.set_state(callback.from_user.id, UserRequest.checkInDate, callback.message.chat.id)
        # with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as bdata:
        #     bdata['checkInDate'] = 'asd'
        # # print(bdata.keys())
        #
        #
        # bot.send_message(callback.from_user.id, "TUT")






@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def cal_id_two(c):
    result, key, step = DetailedTelegramCalendar(calendar_id=2).process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
        print(c.data)
    elif result:
        bot.edit_message_text(f"You selected {result}",
                              c.message.chat.id,
                              c.message.message_id)
        print("ID = 2")

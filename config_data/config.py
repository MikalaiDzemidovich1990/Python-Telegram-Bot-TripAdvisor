import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('lowprice', "Вывеsadsdсти справку"),
    ('help', "Вывести справку"),
    ('lowprice', "Вывести самые дешевые")
)


# 1. lowprice
# 2. highprice
# 3. bestdeal





# 1. City
# 2. Check In
# 1. Check Out
# 1. Photo
# 1. CountPhoto

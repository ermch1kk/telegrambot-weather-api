import telebot
import requests
import json

bot = telebot.TeleBot('your token') # token we take in botfather
WeatherAPI = 'your token' # token we take in https://openweathermap.org/api

# also u can move tokens to .env file

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hey, u pressed /start. Lets go!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'weather':
        bot.send_message(message.chat.id, 'Write the name of the city!')
        bot.register_next_step_handler(message, get_weather)


def get_weather(message): 
    city = message.text.strip().lower()
    print(city)
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=en&appid={WeatherAPI}&units=metric")
    data = json.loads(res.text)
    bot.reply_to(message, f'Now the weather is: {data["main"]["temp"]}')


bot.polling(non_stop=True)

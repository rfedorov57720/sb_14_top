import telebot

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(Токен)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    print('message')
@bot.message_handler(commands=['Привет'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['Пока'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
print('start')
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
 try:
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
 except:
    bot.reply_to(message, 'введите команду в формате /heh <число>')
bot.polling()

import telebot
import random, os
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("ТОКЕН")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! этот бот для того что бы вам рассказать вам какие и куда вещи надо выбрасывать. напишите '/tw_ty' и подпишите на анг. языке что вы хотите выбросить. если это слово-сочитание из 2-3 слов то между ними поставьте нижние подчеркивание.")

@bot.message_handler(commands=['tw_ty'])
def start(message):
    try:
        mes = message.text.split()
        if mes[1] == 'Batteries':
            bot.reply_to(message, 'Вот места где перерабатывают батареи: https://maps.app.goo.gl/xSEJb3bEgFRg81jf9')
        elif mes[1] == 'Mercury_Lamps':
            bot.reply_to(message, 'Вот места где перерабатывают Ртутные лампы: https://maps.app.goo.gl/pBn8iF6WutEsQsoDA')
    except:
        bot.reply_to(message, 'это должно быть то что вы хотите выбросить!')



bot.infinity_polling()

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Замените на свой токен, если будете использовать вручную
TOKEN = "7748081581:AAEAk_JDauMdfp3VycHlGZJor5jvWuDuw9c"

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start и /экспресс
@bot.message_handler(commands=['start', 'экспресс'])
def send_express(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='🔥 ЗАБРАТЬ ЭКСПРЕСС 🔥', url='https://t.me/+O-kSuCsJrrw3ZjEy')
    markup.add(btn)

    with open('img/express.png', 'rb') as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption="""❗ Уверенный экспресс повышенной проходимости уже ждёт тебя ❗

Переходи и забирай пресс с кф 5+ 👇👇👇""",
            reply_markup=markup
        )

# Запуск бота
print("Бот запущен...")
bot.infinity_polling()

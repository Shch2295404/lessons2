import telebot
import datetime
import random
import time
import threading



TOKEN = 'здесь token бота'
bot = telebot.TeleBot(TOKEN)

# Факты о воде для бота
WATER_FACTS = [
    "Вода на Земле может быть старше самой Солнечной системы: Исследования показывают, что от 30% до 50% воды в наших океанах возможно присутствовала в межзвездном пространстве еще до формирования Солнечной системы около 4,6 миллиарда лет назад.",
    "Горячая вода замерзает быстрее холодной: Это явление известно как эффект Мпемба. Под определенными условиями горячая вода может замерзать быстрее, чем холодная, хотя ученые до сих пор полностью не разгадали механизм этого процесса.",
    "Больше воды в атмосфере, чем во всех реках мира: Объем водяного пара в атмосфере Земли в любой момент времени превышает объем воды во всех реках мира вместе взятых. Это подчеркивает важную роль атмосферы в гидрологическом цикле, перераспределяя воду по планете."
]
# Время для напоминаний
REMINDER_TIMES = ["09:00", "15:55", "17:00", "21:00"]


#    Обрабатывает команду /start для начала разговора с ботом.
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить воду 9:00 13:00 17:00 21:00. /start - начать общение!\n/help - описание команд')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


#    Обрабатывает команду /help для вывода информации о боте.
@bot.message_handler(commands=['help'])
def help_bot(message):
    help_text = "Доступные команды:\n/start - начать общение с ботом\n/help - вывести это сообщение\n/fact - факты о воде\nИли введите слово 'Вода' и я напомню тебе о воде"
    bot.reply_to(message, help_text)


#    Обрабатывает команду /fact для вывода случайного факта о воде.
@bot.message_handler(commands=['fact'])
def fact_message(message):
    fact = random.choice(WATER_FACTS)
    bot.send_message(message.chat.id, f'Лови факт о воде: {fact}')


#    Обрабатывает текстовые сообщения для предоставления ответов на основе их содержания.
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    text = message.text.lower()
    if text == "вода":
        bot.send_message(message.chat.id, random.choice(WATER_FACTS))
    else:
        bot.send_message(message.chat.id, "Извините, я не понимаю запроса.")


#    Основная функция для напоминания о выпивке воды.
def send_reminders(chat_id):
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now in REMINDER_TIMES:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)


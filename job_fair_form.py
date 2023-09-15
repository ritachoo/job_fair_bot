import pip

pip.main(['install', 'pytelegrambotapi'])

import telebot
from telebot import types

token = '6130393182:AAFVoEM-572mBzw6JvWEgit6NoUXkg47Gys'
statistic_chat_id = '-1001938030768'

# Создаем бота
bot = telebot.TeleBot(token)
bot.remove_webhook()


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # Сохраняем ID чата, чтобы потом отправить ответы в другой канал
    chat_id = message.chat.id
    with open('img/omp_start.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    bot.send_message(chat_id, '👋Привет! Это бот компании "Открытая Мобильная Платформа". Чтобы получить возможность '
                              'попасть к нам на стажировку, оставь информацию о себе. Для начала, давай познакомимся. '
                              'Напиши свои имя и фамилию👇')
    # Устанавливаем состояние "ожидание имени"
    bot.register_next_step_handler(message, ask_name)


# Обработчик ответа на вопрос "Твое имя?"
def ask_name(message):
    chat_id = message.chat.id
    # Сохраняем имя в переменную
    name = message.text
    # Создаем кнопки с вариантами ответов
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(types.KeyboardButton('Ок, продолжим'))
    # Задаем следующий вопрос
    bot.send_message(chat_id, 'Приятно познакомиться, ' + name + '! Немного о нашей компании: Мы занимаемся '
                                                                 'разработкой и внедрением первой отечественной '
                                                                 'мобильной ОС Аврора и платформы управления '
                                                                 'корпоративными мобильными устройствами Аврора '
                                                                 'Центр, а также других решений, которые позволяют '
                                                                 'строить доверенную мобильную среду, гарантируя '
                                                                 'повышение производительности и защиту '
                                                                 'чувствительной информации. А теперь немного '
                                                                 'о тебе...', reply_markup=markup)
    # Устанавливаем состояние "ожидание инфо"
    bot.register_next_step_handler(message, ask_info, name)


# Обработчик ответа на информацию о компании"
def ask_info(message, name):
    chat_id = message.chat.id
    # Создаем кнопки с вариантами ответов
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(types.KeyboardButton('1'))
    markup.row(types.KeyboardButton('2'))
    markup.row(types.KeyboardButton('3'))
    markup.row(types.KeyboardButton('4'))
    # Задаем следующий вопрос
    bot.send_message(chat_id, 'Расскажи, на каком курсе ты учишься?', reply_markup=markup)
    # Устанавливаем состояние "ожидание курса обучения"
    bot.register_next_step_handler(message, ask_year_of_study, name)


# Обработчик ответа на вопрос "Курс обучения?"
def ask_year_of_study(message, name):
    chat_id = message.chat.id
    # Сохраняем курс обучения в переменную
    year_of_study = message.text
    # Удалаем варианты предыдущего вопроса
    markup = types.ReplyKeyboardRemove()
    # Задаем следующий вопрос
    bot.send_message(chat_id, 'Отлично! Напиши свое направление обучения', reply_markup=markup)
    # Устанавливаем состояние "ожидание направления стажировки"
    bot.register_next_step_handler(message, ask_course_of_study, name, year_of_study)


# Обработчик ответа на вопрос "Направление обучения?"
def ask_course_of_study(message, name, year_of_study):
    chat_id = message.chat.id
    # Сохраняем возраст в переменную
    course_of_study = message.text
    # Создаем кнопки с вариантами ответов
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(types.KeyboardButton('Ручное тестирование'))
    markup.row(types.KeyboardButton('Автоматизированное тестирование'))
    markup.row(types.KeyboardButton('Разработка'))
    markup.row(types.KeyboardButton('Инфраструктура разработки (DevOps)'))
    # Задаем следующий вопрос
    bot.send_message(chat_id, 'Круто! А теперь выбери какое направление стажировки тебе интересно?',
                     reply_markup=markup)
    # Устанавливаем состояние "ожидание направления стажировки"
    bot.register_next_step_handler(message, ask_internship_direction, name, year_of_study, course_of_study)


# Обработчик ответа на вопрос "Направление подготовки?"
def ask_internship_direction(message, name, year_of_study, course_of_study):
    chat_id = message.chat.id
    # Сохраняем возраст в переменную
    internship_direction = message.text
    # Добавляем кнопку сайта
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url='https://omp.ru/'))

    # Получаем telegram_id студента
    telegram_id = message.from_user.id
    username = message.from_user.username
    # Отправляем ответы в другой канал Telegram
    bot.send_message(statistic_chat_id, f'Студент: {name}\nКурс обучения: {year_of_study}\nНаправление обучения: '
                                        f'{course_of_study}\nЖелаемое направление стажировки: {internship_direction}\n'
                                        f'TelegramID: {telegram_id}\nUsername: {username}')
    with open('img/omp_finish.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    bot.send_message(chat_id, 'Спасибо за ответы! Мы обязательно свяжемся с тобой по поводу указанного направления '
                              'стажировки. А пока ты можешь узнать о нас более подробно на нашем сайте',
                     reply_markup=markup)
    # Устанавливаем состояние "ожидание команды"
    bot.register_next_step_handler(message, start_message)


# Обработчик неизвестной команды
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Извини, я не знаю такой команды. Напиши /start, чтобы начать.')


# Запуск бота
# bot.polling(none_stop=True)
bot.infinity_polling()

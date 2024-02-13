import telebot
from telebot import types  # для указание типов
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import config
from html.parser import HTMLParser
from byShopper import create_inline_keyboard, menu_inline_keyboard, guide_keyboard

# Создаем экземпляр бота
bot = telebot.TeleBot(config.TOKEN)  # токен лежит в файле config.py

# фотографии
photo = open(r'images\photo_2023-07-31_23-06-48.jpg', 'rb')  # вставьте сюда путь к вашему фото
photo_2 = open(r'images\photo_2023-07-31_23-06-48 (2).jpg', 'rb')
photo_3 = open(r'images\photo_2023-06-12_15-03-40.jpg', 'rb')

# Создаем клавиатуру с кнопками
#main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#main_menu_keyboard.add(KeyboardButton('Назад в меню'))

@bot.message_handler(func=lambda message: message.text == 'Назад в меню')
def handle_back_to_menu(message):
    markup = menu_inline_keyboard() # создание inline клавиатуры
    #bot.send_message(message.chat.id, 'Вы вернулись в меню!', reply_markup=main_menu_keyboard)
    bot.send_message(message.chat.id, 'Вы вернулись в меню!', reply_markup=markup)

# декоратор команды START
@bot.message_handler(commands=['start'])  # создаем команду для кнопки "start"
def start_message(message):
    # Создаем объект для inline клавиатуры
    markup = menu_inline_keyboard() # создание inline клавиатуры
    # Получаем имя пользователя
    first_name = message.from_user.first_name
    # Отправляем сообщение с именем пользователя
    bot.send_photo(message.chat.id, photo, caption=f'<b>Привет, {first_name}!</b>\nТЕЕЕЕЕЕЕКСТТТТТ\n<b>Нажимай на нужную кнопку</b>'.format(message.from_user), reply_markup=markup, parse_mode='html')
    
    # Обработчик событий 
    @bot.callback_query_handler(func = lambda call: True )
    def answer(call):
        if call.data == 'guide_':
                markup = guide_keyboard()
                bot.send_photo(message.chat.id, photo_2, caption=f'Для получения <b>бесплатного</b> гайда \n<b>ПОДПИШИСЬ</b> на мой канал и нажимай кнопку <b>готово</b>'.format(message.from_user), reply_markup=markup, parse_mode='html')

        #Обработчик кода кнопки "ГОТОВО"
        if call.data == 'done':
                # ID канала, на который вы хотите проверить подписку
                channel_id = '@...'
                # ID пользователя, которого вы хотите проверить
                user_id = message.from_user.id
                # Выполняем проверку подписки пользователя
                response = bot.get_chat_member(channel_id, user_id)
                # Проверяем статус пользователя
                if response.status == 'left':
                        bot.send_message(message.chat.id, text= "Доступ ограничен из-за отсутствия подписки на ресурс.")
                elif response.status == 'member' or response.status == 'administrator' or response.status == 'creator':
                        bot.send_message(message.chat.id, text= "Спасибо за Ваше доверие!\nВот Ваш гайд:")
                        bot.send_document(message.chat.id, open(r'documents\guide.docx', 'rb'))
                
        # Меню (покупка шоппера)
        if call.data == 'buyShopper_':
                keyboard = create_inline_keyboard()
                bot.send_photo(message.chat.id, photo_3, caption=f'<b>Привет!</b>\n"Текст\nМы стремимся предложить отличное качество одежды и стильный дизайн по доступной цене.\n<b>Нажимай на нужную кнопку, чтобы получить всю необходимую информацию о ценах, наличии товара, а также сделать заказ!</b>'.format(message.from_user), reply_markup=keyboard, parse_mode='html')
                     
        if call.data == 'fird':
                 bot.send_message(call.message.chat.id, 'Текст')
    

        if call.data == 'back':
                handle_back_to_menu(message)
                  
                      
                
        
        
        #bot.answer_callback_query(callback_query_id=call.id) #присылает сообщения сам





bot.polling(none_stop=True)
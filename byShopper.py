from telebot import types  # для указание типов

chan_id = ...

def create_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    buttonDesignerink = types.InlineKeyboardButton(text='text', callback_data='subscribeDesignerink', url= f'...{chan_id}')
    buttonBack = types.InlineKeyboardButton('Назад', callback_data='back')
    keyboard.add(buttonDesignerink)
    keyboard.add(buttonBack)
    
    return keyboard
 
def menu_inline_keyboard():    
    # Создаем объект для inline клавиатуры
    markup = types.InlineKeyboardMarkup() # создание inline клавиатуры

    button1 = types.InlineKeyboardButton(text='Получить бесплатный гайд', callback_data='guide_')
    button2 = types.InlineKeyboardButton(text='Купить шопер', callback_data='buyShopper_')
    button3 = types.InlineKeyboardButton(text='Мой тг канал', callback_data='fird')
    
    markup.add(button1) # вывод кнопоки 1
    markup.add(button2) # вывод кнопоки 2
    markup.add(button3) # вывод кнопоки 3

    return markup
   
def guide_keyboard():
    # Создание inline-клавиатуры
    markup = types.InlineKeyboardMarkup()
    # Создание кнопки для проверки подписки

    subscription_button = types.InlineKeyboardButton(text='ПОДПИСАТЬСЯ', callback_data='subscribe', url= f'...{chan_id}')
    done_button = types.InlineKeyboardButton(text='ГОТОВО', callback_data='done')

    markup.add(subscription_button)
    markup.add(done_button)

    return markup
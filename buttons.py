from telebot import types

channal_id = ...

# Создание кнопок
button1 = types.KeyboardButton('Кнопка 1')
button2 = types.KeyboardButton('Кнопка 2')
button3 = types.KeyboardButton('Кнопка 3')

buttonDesignerink = types.InlineKeyboardButton(text='text', callback_data='subscribeDesignerink', url= f'...{channal_id}')
buttonBack = types.InlineKeyboardButton('Назад')

# Создание inline клавиатуры 
keyboard1 = types.InlineKeyboardMarkup()



# Создание клавиатуры с кнопками
keyboard = types.ReplyKeyboardMarkup()
keyboard.row(button1, button2)
keyboard.row(button3)

# Экспорт кнопок для использования в основном файле
buttons = {
    'keyboard': keyboard,
    'button1': button1,
    'button2': button2,
    'button3': button3
}
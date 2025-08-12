from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Button:
    def __init__(self, text, callback):
        self.text = text
        self.callback = callback
    def __repr__(self):
        return self.text + '///' + self.callback

class Buttons:
    def __init__(self, buttons, rows):
        keyboard = []
        ind = 0
        for row in rows:
            tmp = []
            for i in range(row):
                tmp.append(InlineKeyboardButton(text=buttons[ind].text, callback_data=buttons[ind].callback))
                ind += 1
            keyboard.append(tmp)
            
        
        self.keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        
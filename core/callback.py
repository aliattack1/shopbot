from aiogram import Dispatcher, Router
from aiogram.types import CallbackQuery
from core import button
class pagination:
    def __init__(self, itemperpage, items, dp:Dispatcher):
        self.pages = []
        ind = 0 
        while ind < len(items):
            tmp = []
            for i in range(itemperpage):
                tmp.append(items[ind])
                ind+=1
            tmp.append('<')
            tmp.append('>')
            self.pages.append(tmp)
        buttons, rows = transform(self.pages[0], 0)
        self.mainkeyboard = button.Buttons(buttons, rows).keyboard
        
        
        self.router = Router()
        
        @self.router.callback_query(lambda c: c.data and c.data.startswith('page:'))
        async def page_handler(callback: CallbackQuery):
            
            page = int(callback.data.split(":")[1])
            buttons, rows = transform(self.pages[page], page)
            await callback.message.edit_reply_markup(reply_markup=button.Buttons(buttons, rows).keyboard)
            await callback.answer()
        

def transform(page, pageid):
    buttons = []
    ind = 0
    for item in page:
        if item == '<':
            buttons.append(button.Button(item, f'page:{pageid-1}'))
        elif item == '>':
            buttons.append(button.Button(item, f'page:{pageid+1}'))
        else:
            buttons.append(button.Button(item, item))
            
        ind += 1
    return buttons, [2 for i in range(int(ind/2))]
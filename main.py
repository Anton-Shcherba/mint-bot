import os
from aiogram import Bot, Dispatcher, executor, types
from background import keep_alive  #импорт функции для поддержки работоспособности

token = os.environ['TOKEN']
bot = Bot(token)
dispatcher = Dispatcher(bot)

@dispatcher.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
  await message.answer('start msg')

keep_alive()  #запускаем flask-сервер в отдельном потоке. Подробнее ниже...

if __name__ == "__main__" :
    executor.start_polling(dispatcher, skip_updates=True)

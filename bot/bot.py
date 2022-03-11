#########################################################
#                      БИБЛИОТЕКИ                       #
#########################################################

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#########################################################
#                        МОДУЛИ                         #
#########################################################

from config import TOKEN
from utils import TestStates
from messages import MESSAGES
from random import randint
from sqliter import SQLighter
from sqliter import SQLreader
import markups as nav

#########################################################
#                    ИНИЦИАЛИЗАЦИЯ                      #
#########################################################

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = SQLighter('db.db')
db_out = SQLreader('db.db')


#########################################################
#                        КОМАНДЫ                        #
#########################################################

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    db.add_subscriber(message.from_user.id)
    await message.reply(MESSAGES['start'], reply_markup=nav.mainMenu, reply=False)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'], reply=False)


#########################################################
#                  ОБРАБОТКА СООБЩЕНИЙ                  #
#########################################################

@dp.message_handler()
async def sorting_messages(message: types.Message):
    if message.text == "Главное меню":
        state = dp.current_state(user=message.from_user.id)
        await state.reset_state()
        await bot.send_message(message.from_user.id, MESSAGES['what'], reply_markup=nav.mainMenu)


    elif message.text == 'Узнать погоду':
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(TestStates.all()[1])
        nav.RaisingWeatherMenu(message.from_user.id)
        await bot.send_message(message.from_user.id, MESSAGES['ask_place'], reply_markup=nav.weatherMenu)

    elif message.text == 'Рандомное число':
        await bot.send_message(message.from_user.id, f'Ваше число: {randint(-1000000, 1000000)}')

    elif message.text == 'О боте':
        await message.reply(MESSAGES['help'], reply=False)

#########################################################
#                     ОПОВЕЩЕНИЯ                        #
#########################################################

@dp.message_handler(state=TestStates.TEST_STATE_2)
async def reminding_ilter(message: types.Message):
    if message.text == 'Указать город':
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(TestStates.all()[3])
        await bot.send_message(message.from_user.id, MESSAGES['ask_place'], reply_markup=nav.remSetMenu)

    elif message.text == 'Установить часовой пояс':
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(TestStates.all()[4])
        await bot.send_message(message.from_user.id, MESSAGES['utc'], reply_markup=nav.remSetMenu)

    elif message.text == 'Указать время напоминания':
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(TestStates.all()[5])
        await bot.send_message(message.from_user.id, MESSAGES['time'], reply_markup=nav.remSetMenu)

    elif message.text == 'Назад':
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(TestStates.all()[1])
        await bot.send_message(message.from_user.id, MESSAGES['ask_place'], reply_markup=nav.weatherMenu)


#########################################################
#             ОТКЛЮЧЕНИЕ МАШИНЫ СОСТОЯНИЙ               #
#########################################################

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


#########################################################
#                      ИСПОЛНЕНИЕ                       #
#########################################################

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from sqliter import SQLreader

db_out = SQLreader('db.db')



#global buttons
btnMainMenu = KeyboardButton('Главное меню')
btnCancel =KeyboardButton('Назад')


#main menu
btnRandom = KeyboardButton('Рандомное число')
btnInfo = KeyboardButton('О боте')
btnWeather = KeyboardButton('Узнать погоду')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnInfo, btnWeather)

#weather menu
btnSetReminder = KeyboardButton('Потсавить оповещение')
weatherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnSetReminder, btnMainMenu)
def RaisingWeatherMenu(user_id):
	latest_place = db_out.read_informarion(user_id)
	#latest_place = latest_place[4]
	
	if latest_place != None:
		btnLtestPlace = KeyboardButton(f'{latest_place}')
		weatherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnLtestPlace, btnSetReminder, btnMainMenu)
		print(weatherMenu)
	else:
		weatherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnSetReminder, btnMainMenu)




#reminding menu
btnSetUTC = KeyboardButton('Установить часовой пояс')
btnSetPlace = KeyboardButton('Указать город')
btnTime = KeyboardButton('Указать время напоминания')
remindingMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnSetPlace, btnSetUTC, btnTime, btnCancel, btnMainMenu)

#reminding settings menu
remSetMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnCancel, btnMainMenu)





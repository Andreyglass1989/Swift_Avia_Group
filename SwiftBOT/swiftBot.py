# _*_ coding: utf-8 _*_

import telebot
import const

bot = telebot.TeleBot(const.token)

upd = bot.get_updates()
last_upd=upd[-1]
message_from_user = last_upd.message

print(bot.get_me())

def log(message, answer):
	print("\n -------------")
	from datetime import datetime
	print(datetime.now())
	print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
																	message.from_user.last_name,
																	str(message.from_user.id),
																	message.text))
	print(answer)




@bot.message_handler(commands=['help'])
def handle_text(message):
	bot.send_message(message.chat.id, """ Мои возможности весьма ограничены """)


@bot.message_handler(content_types=['text'])
def handler_text(message):
	answer = u"ты не умеешь играть"
	if message.text == 'a':
		answer = u"Б"
		bot.send_message(message.chat.id, answer)
		log(message, answer)
	elif message.text == 'b':
		answer = u"A"
		bot.send_message(message.chat.id, answer)
		log(message, answer)
	else:
		bot.send_message(message.chat.id, answer)
		log(message, answer)



bot.polling(none_stop=True, interval=0)
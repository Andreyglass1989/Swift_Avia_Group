from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='Avia Logistic',
	avatar='http://viber.com/avatar.jpg',
	auth_token='485a124213a7d7d9-9f3d9d22def5a3ce-ab15fd7f9dae9b25'
)
viber = Api(bot_configuration)
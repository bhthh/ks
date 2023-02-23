import telebot

token ="5847365664:AAE-VbpGfVo4AL5Ihk2pHwL2rJGX6jlLPkM"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
 bot.send_message(message.chat.id,f"اهلا بك في بوت اضهار معلوماتك • ارسل /id لمعرفه ايديك • ارسل /u لمعرفه يوزرك")
 
@bot.message_handler(commands=["id"])
def info(message):
	i = message.from_user.id
	u = message.from_user.username
	infos = "id  :  {} ".format(i,u)
	bot.send_message(message.chat.id,infos)

@bot.message_handler(commands=["u"])
def info(message):
	u = message.from_user.username
	infos = "username :  {}".format(u)
	bot.send_message(message.chat.id,infos)

bot.infinity_polling()

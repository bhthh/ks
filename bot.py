import telebot
import app.json
import config
import Procfile
import requirements.txt
import runtime.txt
import Dockerfile

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

import telebot
from tokens import * 
import os 

TOKEN = telegrambot
chat_id = adminchatid


bot = telebot.TeleBot(TOKEN)

#    bot.send_message(chat_id, f'{newhashsum}')



if os.stat("/opt/error").st_size != 0:

   f = open("/opt/error","r")
   data = f.read()
   print(data)
   bot.send_message(chat_id, f'{data}')


   file = open('/opt/error', 'w')
   file.close()

else: print("Empty")



#print(hashs)
#bot.send_message(chat_id, f'{hash}')



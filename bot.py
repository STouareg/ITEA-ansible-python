import telebot
from tokens import * 
import hashlib

TOKEN = telegrambot
chat_id = adminchatid


bot = telebot.TeleBot(TOKEN)


file_with_hashsum = open("/home/admturyk/hash")
hashsum = file_with_hashsum.read()
file_with_hashsum.close() 

with open("/opt/error", "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)
    newhashsum = file_hash.hexdigest()

if newhashsum != hashsum: 
    print(newhashsum)
    bot.send_message(chat_id, f'{newhashsum}')
    
    file_1 = open("/home/admturyk/hash", "w")
    file_1.write(str(hashsum))
    file_1.close()

else: print("hash is the same")



#print(hashs)
#bot.send_message(chat_id, f'{hash}')



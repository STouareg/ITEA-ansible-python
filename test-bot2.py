import telebot
from tokens import * 
import hashlib

TOKEN = telegrambot
chat_id = adminchatid


bot = telebot.TeleBot(TOKEN)


file_with_hashsum = open("/home/admturyk/hash", "r")
hashsum = file_with_hashsum.read()
file_with_hashsum.close() 
print("Hash is  ", f"{hashsum}")


with open("/opt/error", "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)
    newhashsum = file_hash.hexdigest()

if newhashsum != hashsum: 
    print("newhashsum is ", f"{newhashsum}")
#    bot.send_message(chat_id, f'{newhashsum}')
#    file_error = open("/opt/error", "r")
#    print(*file_error)
#    file_error.close()
    

    file_hash = open("/home/admturyk/hash", "w")
    file_hash.write(str(hashsum))
    file_hash.close()

else: print("hash is the same")



#print(hashs)
#bot.send_message(chat_id, f'{hash}')



import telebot
import time
import os
from subprocess import check_output

# Обход роскомнадзора
#from telebot import apihelper
#apihelper.proxy = { 'https': 'socks5h://77.81.226.18:1080' }     

token     = 'ТОКЕН' # ТОКЕН
AdminList = 'ID' # ВАШ ID
bot       = telebot.TeleBot(token)

# Сообщение при старте (/start)
ComStart  = 'Bash приветствует тебя, мой друг!' 

R  = '\033[31m' # red
G  = '\033[32m' # green
C  = '\033[36m' # cyan
W  = '\033[0m'  # white
B  = '\033[30m' # black
LG = "\033[37m" # LightGray
M  = "\033[35m" # Magenta

version = 'v0.0.1'

def banner():
	os.system('clear')
	print (LG +  '''
████████████████████████████████
████░░██░░░░██░░████████████████
██░░██░░████░░██░░██████████████
░░██░░██░░░░██░░██░░████████████
░░██░░████░░██░░██░░░░██████████
██░░░░░░░░██░░░░░░░░██░░████████
██████░░██░░████░░██░░██░░██████
████░░██░░░░██████░░░░██░░██████
████░░████████████████░░████████
██████░░██░░░░░░░░░░██░░████████
████████░░░░██████░░░░██████████
██░░░░████░░░░░░░░░░████████████
██░░██░░████████████████████████
██░░░░██████░░████░░░░░░████████
██░░██░░██░░██░░████░░██████████
██░░░░██████░░██████░░██████████''' + W)
	print('\n' + G + '[>]' + W + ' Created By : ' + W + '@Oirefive')
	print(G + '[>]' + W + ' Version    : ' + W + version) 
def InfoAdminList():  
    print('\n' + G + '[>]' + M + ' AdminList  : ' + W + AdminList + '\n')

# Команда /start > исполнить (помощь по командам)
@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.chat.id, ComStart)
 
# Любой text > исполнить (исполняется команда на Lunix сервере)
@bot.message_handler(content_types=["text"])
def main(message):
    #print('> "def main(message)" работает!')
    if str(message.chat.id) == AdminList: # Избранный = отправитель > Можно
        #print('"if (AdminList == message.chat.id):" выполнено успешно!')
        Command = message.text # Отправленное сообщение.
        try: # Исполнить команду из сообщения
            #print('Запрос на исполнение "' + Command + '"')
            bot.send_message(message.chat.id, check_output(Command, shell = True))
        except: # В случае ошибки
            print('> Возможно ошибка: "' + Command + '"')
banner(); InfoAdminList();
 
if __name__ == '__main__':
    bot.polling(none_stop=True)
	
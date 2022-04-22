import telebot
from config import API_TOKEN
from parser import Parser
from jobsarray import JobsArray
from telebot import types
from screenshot import ScreenShoter
import requests

class BotSooliks:

    def init_telegram_bot(token):
        parser = Parser(url_btc_usd='https://yobit.net/api/3/ticker/btc_usd',url_eth_usd='https://yobit.net/api/3/ticker/eth_usd',url_cybershoke='https://cybershoke.net/home',url_crazytime='https://spikeslot.com/live-stats/crazy-time/row', url_warface_online='https://warface-statistics.firebaseapp.com/')
        jobsarray = JobsArray()
        screenshoter = ScreenShoter()
        bot=telebot.TeleBot(token)
        

        @bot.message_handler(commands=['start'])
        def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Курс usd к btc")
            #btn2 = types.KeyboardButton("❓ Задать вопрос")
            btn3 = types.KeyboardButton("crazytime-screen")
            btn4 = types.KeyboardButton("Курс usd к eth")
            btn5 = types.KeyboardButton("❗❗❗Все курсы криптовалют❗❗❗")
            btn6 = types.KeyboardButton("Онлайн CyberShoke")
            btn7 = types.KeyboardButton("Сколько подряд спинов не выпадала бонуска в CrazyTime")
            #btn8 = types.KeyboardButton("Онлайн Warface")
            #btn9 = types.KeyboardButton("иксы crazytime2.0")
            
            markup.add(btn1,btn4,btn3,btn5,btn6,btn7)
            bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот который может показать тебе курсы валют и многое другое!".format(message.from_user), reply_markup=markup)

    


        @bot.message_handler(content_types=["text"])
        def send_text(message):
            
            
            if message.text.lower()=="курс usd к btc":
                bot.send_message(message.chat.id,parser.get_data("btc_usd"))
                print("Вызвана команда узнать курс btc",parser.get_data("btc_usd"))

            elif message.text.lower()=="курс usd к eth":
                bot.send_message(message.chat.id,parser.get_data("eth_usd"))
                print("Вызвана команда узнать курс eth",parser.get_data("eth_usd"))   

            elif message.text.lower()=="crazytime-screen":
                photo = open(screenshoter.screen(url="https://casinoscores.com/crazy-time/"), 'rb')
                bot.send_photo(message.chat.id, photo)
                print("Вызвана команда скрин крейзитайм")

            elif message.text.lower()=="❗❗❗все курсы криптовалют❗❗❗":
                photo = open(screenshoter.screen(url="https://bitinfocharts.com/ru/crypto-kurs/"), 'rb')
                bot.send_photo(message.chat.id, photo)
                print("Вызвана команда курсы")

            elif message.text.lower()=="онлайн cybershoke":
                bot.send_message(message.chat.id,parser.get_data("online_cybershoke"))
                print("Вызвана команда узнать онлайн cybershoke: ",parser.get_data("online_cybershoke"))  

            elif message.text.lower()=="сколько подряд спинов не выпадала бонуска в crazytime":
                list_of_bonuses = parser.get_data("stat_x-crazytime")
                bot.send_message(message.chat.id,text='Единица не выпадала:') 
                if list_of_bonuses[0]=='0 Spin':
                    bot.send_message(message.chat.id,text='Единица выпала только что!') 
                else:
                    bot.send_message(message.chat.id,list_of_bonuses[0]) 

                bot.send_message(message.chat.id,text='Двойка не выпадала:') 
                if list_of_bonuses[1]=='0 Spin':
                    bot.send_message(message.chat.id,text='Двойка выпала только что!') 
                else:
                    bot.send_message(message.chat.id,list_of_bonuses[1]) 

                bot.send_message(message.chat.id,text='Пятерка не выпадала:') 
                if list_of_bonuses[2]=='0 Spin':
                    bot.send_message(message.chat.id,text='Пятерка выпала только что!') 
                else:
                    bot.send_message(message.chat.id,list_of_bonuses[2]) 

                bot.send_message(message.chat.id,text='Десятка не выпадала:') 
                if list_of_bonuses[3]=='0 Spin':
                    bot.send_message(message.chat.id,text='Десятка выпала только что!') 
                else:
                    bot.send_message(message.chat.id,list_of_bonuses[3]) 
                
                bot.send_message(message.chat.id,text='CashHunt не выпадал:') 
                if list_of_bonuses[4]=='0 Spin':
                    bot.send_message(message.chat.id,text='CashHunt выпал только что!') 
                else:
                    bot.send_message(message.chat.id,list_of_bonuses[4]) 

                bot.send_message(message.chat.id,text='Pachinko не выпадал:') 
                if list_of_bonuses[5]=='0 Spin':
                    bot.send_message(message.chat.id,text='Pachinko выпал только что!') 
                else:
                    bot.send_message(message.chat.id,list_of_bonuses[5]) 

                bot.send_message(message.chat.id,text='CoinFlip не выпадал:') 
                if list_of_bonuses[6]=='0 Spin':
                    bot.send_message(message.chat.id,text='CoinFlip выпал только что!') 
                else:
                    bot.send_message(message.chat.id,list_of_bonuses[6]) 

                bot.send_message(message.chat.id,text='CrazyTime не выпадал:') 
                if list_of_bonuses[7]=='0 Spin':
                    bot.send_message(message.chat.id,text='CrazyTime выпал только что!') 
                else:
                    bot.send_message(message.chat.id,list_of_bonuses[7]) 

                #bot.send_message(message.chat.id,text='Шанс выпадения CoinFlip: ') 
                #formula_crazytime=list_of_bonuses[6]
                #for char in ('S', 'p', 'i', 'n'):
                #formula_crazytime = formula_crazytime.replace(char, '')
                #float(formula_crazytime)+100.3/12.6
                #print(formula_crazytime)
                #bot.send_message(message.chat.id,formula_crazytime) 


                
                

            elif message.text.lower()=="онлайн warface":
                print("Вызвана команда узнать онлайн варфейс",parser.get_data("warface_online")) 
                bot.send_message(message.chat.id,parser.get_data("warface_online")) 

            else:
                bot.send_message(message.chat.id, "Неизвестная команда!")     



    

        bot.polling()
        
    init_telegram_bot(API_TOKEN)

    


    

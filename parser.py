
from lib2to3.pgen2 import driver
import requests
from bs4 import BeautifulSoup as BS
from lxml import etree
from selenium import webdriver
from screenshot import ScreenShoter
class Parser:


    def __init__(self,url_btc_usd,url_eth_usd,url_cybershoke,url_crazytime,url_warface_online):
        self.url_btc_usd=url_btc_usd
        self.url_eth_usd=url_eth_usd
        self.url_cybershoke=url_cybershoke
        self.url_crazytime = url_crazytime
        self.url_warface_online=url_warface_online
        
      
    def get_data(self,value):
        if value=='btc_usd':
            req = requests.get(self.url_btc_usd)
            response = req.json()
            sell_price = response["btc_usd"]["sell"]
            return sell_price
        elif value=='eth_usd':
            req = requests.get(self.url_eth_usd)
            response = req.json()
            sell_price = response["eth_usd"]["sell"]
            return sell_price
        elif value=='online_cybershoke':
            req = requests.get(self.url_cybershoke)
            html = BS(req.content,'html.parser')
            items=html.select('#global-all-online-players')
            return [c.text for c in items]
        elif value=='stat_x-crazytime':
            req = requests.get(self.url_crazytime)
            html = BS(req.content,'html.parser')
            #items=html.select("tbody[class='MuiTableBody-root']")
            items=html.select("p[style='font-weight:bold;font-size:1.5rem']")
            print("Вызвана команда иксы крейзи тайм")
            print([c.text for c in items]) 
            return [c.text for c in items]
        elif value=='warface_online':
            req = requests.get(self.url_warface_online)
            html = BS(req.content,'html.parser')
            items=html.select("div[class='line']")
            print(items)
            return [c.text for c in items]
        
        
                    
            





# -*- coding: utf-8 -*-
import requests
import json
from wxpy import *
#bot = Bot()
#my_friend = bot.friends().search('谈小罗')
#my_friend.send('Hello, this is from wxpy robot!')
def change_link(APIKEY,TaoBaokey):
    requests_input = 'https://www.taokelu.com/api/v1/parse_tkl?apiKey='+ APIKEY+'&tkl=￥'+TaoBaokey+'￥'
    result = requests.get(requests_input).json()
    return result['data']['raw_url']
def check_ID(APIKEY,TaoBaoID):
    requests_input = 'https://www.taokelu.com/api/v1/query_coupon?apiKey=' + APIKEY + '&&taobao_item_id='+TaoBaoID
    result = requests.get(requests_input).json()
    return result
if __name__ == '__main__':
    #@bot.register(my_friend,TEXT)
    #def print1_messages(msg):
    #    print(msg)
    #embed()

    #change_link('f17a686b4fb2043fdebf9b6667ab5e35','xIQO0Sc5VEH')
    check = check_ID('bd11babe56b5b2df4aa432b8cc1c5fa3', '521057978532')
    print(check)
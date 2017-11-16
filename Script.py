# -*- coding: utf-8 -*-
import requests
import json
from wxpy import *
import csv
from time import strftime

addfriend_request = '加好友'  #自动添加好友的条件
apikey ='f17a686b4fb2043fdebf9b6667ab5e35'  #输入淘客路的apikey   罗睿账号bd11babe56b5b2df4aa432b8cc1c5fa3
invite_text = "请粘贴淘宝分享获取优惠链接"  #任意回复获取的菜单

csv_1 = 'test.csv'   #表格1


bot = Bot(cache_path = True)
bot.enable_puid()  #启用聊天对象的puis属性

def  change_link(APIKEY,TaoBaokey):
    requests_input = 'https://www.taokelu.com/api/v1/parse_tkl?apiKey='+ APIKEY+'&tkl=￥'+TaoBaokey+'￥'
    result = requests.get(requests_input).json()
    return result['data']['raw_url']

def check_ID(APIKEY,TaoBaoID):
    requests_input = 'https://www.taokelu.com/api/v1/query_coupon?apiKey=' + APIKEY + '&&taobao_item_id='+TaoBaoID
    result = requests.get(requests_input).json()
    return result

#写表函数
def table(user, text):
    #提取用户的文本，把有用的写入表里
    time_current = strftime("%Y%m%d %H:%M:%S")
    msg_text = text.split('￥')[0]
    table_list = [str(user.name), msg_text,time_current]
    print(table_list)
    with open(csv_1, 'a', newline='') as request_log:
        write_step = csv.writer(request_log)
        write_step.writerow(table_list)
        request_log.close()



# 注册好友请求类消息
@bot.register(msg_types=FRIENDS,enabled=True)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if addfriend_request in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('机器人自动接受了你的请求,你可以任意回复获取功能菜单，若机器人没回复菜单则表明机器人尚未工作，请等待')

#注册自动回复好友消息
@bot.register(Friend, msg_types=TEXT)
def exist_friends(msg):
    if '复制这条信息' in msg.text.lower():
        key = msg.text.split('￥')[1]
        msg.sender.send('请稍等，后台处理中')
        table(msg.sender, msg.text)
        feedback = change_link(apikey, key)
        taobaoId = feedback[feedback.find('/i')+2:feedback.find('.htm')]
        check_infor = check_ID(apikey, taobaoId)
        print(check_infor)
        msg.sender.send(check_infor['msg'])
    else:
        return invite_text


bot.join()

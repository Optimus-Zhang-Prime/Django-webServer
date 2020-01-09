import smtplib
import pytz
from email.mime.text import MIMEText
import urllib.request
import gzip
import json
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
from datetime import datetime


def howmanyday():
    # 构造一个将来的时间
    Anniversary = datetime.strptime('2019-2-20 8:15:00', '%Y-%m-%d %H:%M:%S')
    # 当前时间
    now = datetime.now()
    # 求时间差
    delta = now-Anniversary
    return delta.days


def sendEmail(header, mess, weather, high, low):
    server = "smtp.163.com"
    sender = "zouhanzhang666@163.com"
    pwd = "Zouhan0903"
    add = "（本邮件由雯雯专属天气助手发送，每天7点自动触发，就算回复 我是憨憨 & I Love ZHZ 也不能退订本服务）"
    text = MIMEText(mess + '\n\n' + '今日天气:' + weather + '\n' + high + '\n' + low + '\n\n\n\n\n\n\n\n' + add)
    text["Subject"] = header
    text["from"] = sender
    mailServer = smtplib.SMTP(server, 25)  # 25为端口号
    mailServer.login(sender, pwd)
    mailServer.sendmail(sender, ["zouhanzhang666@163.com", "1453196338@qq.com", "1623005735@qq.com"], text.as_string())
    mailServer.quit()


# "1623005735@qq.com"
def wenwen():
    city_name = '环翠区'
    type = 0
    mess = "——————————————"
    url1 = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + urllib.parse.quote(city_name)
    weather_data = urllib.request.urlopen(url1).read()
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    day = str(howmanyday())
    header = "今天是我们在一起的第" + day + "天，愿你每天都有好心情！"
    print(weather_data)
    tree = ET.fromstring(weather_data)
    接口消息 = parseString(weather_data)
    今天 = 接口消息.getElementsByTagName('weather')[0]
    天气 = 今天.getElementsByTagName("type")[0]
    高温 = 今天.getElementsByTagName("high")[0]
    低温 = 今天.getElementsByTagName("low")[0]
    指数 = 接口消息.getElementsByTagName('zhishu')
    for 类别 in 指数:
        detail = 类别.getElementsByTagName("detail")[0]
        name = 类别.getElementsByTagName("name")[0]
        value = 类别.getElementsByTagName('value')[0]
        if name.firstChild.data == '雨伞指数' and value.firstChild.data == '带伞':
            mess = detail.firstChild.data
            header = "带伞警告！"
        elif name.firstChild.data == '感冒指数' and value.firstChild.data == '极易发':
            mess = detail.firstChild.data
            header = "防感冒警告！"

    sendEmail(header, str(mess), str(天气.firstChild.data), str(高温.firstChild.data), str(低温.firstChild.data))

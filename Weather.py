# coding:utf-8
# Python --version：2.7.11
# api:魅族天气
import city_transfer_cityID
import urllib2
import json
import os

# 魅族天气API
url = "http://aider.meizu.com/app/weather/listWeather?cityIds="
inputName = raw_input("输入城市名称(enter 'q' to exit):")
if inputName == 'q':
    os._exit(1)

# 获取城市代码
city = city_transfer_cityID.cityname_transfer_cityid(inputName)
url = url + str(city)

# 请求数据并获得响应
req = urllib2.Request(url)
response = urllib2.urlopen(req)
content = response.read()

# 解析获取到的数据
cities_json = json.loads(content)

# 天气情况输出
print "查询城市:", cities_json["value"][0]["city"]

weathers = cities_json['value'][0]['weathers']
print "日期\t\t\t\t\t", "天气\t\t", "温度\t\t"
for index in weathers:
    # print '_'*56
    print index['date'], index['week'] + '\t',
    print index['weather'] + '\t\t',
    print index['temp_night_c'], "℃ ~", index['temp_day_c'], "℃"
    """
    print "|日期:", index['date'], index['week'] + '|\t',
    print "|天气:", index['weather'] + '\t|',
    print "|温度:", index['temp_night_c'], "℃ ~", index['temp_day_c'], "℃|"
    """

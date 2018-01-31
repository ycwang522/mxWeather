#coding:utf-8
import json
import sys, os
"""
该模块功能：
提取城市名称和城市代码
输入城市名称返回对应城市的代码

添加异常处理：
城市名称输入错误时提示错误并要求重新输入
"""

# 容纳换位后的数据：城市.Unicode, 城市代码
cityName_cityID = {}

# 地级市：提取出地级市的城市名称(作为dict的key)和城市代号(作为dict的value)，并存入cityName_cityID
# 其中：对城市名称进行编码，以Unicode编码格式存储
with open('meizu_city.json', 'r') as f:
    data = f.read().decode('gbk').encode('utf-8')
    cities = json.loads(data)
    cityList = cities["cities"]
for city in cityList:
    cityName = city['city'].encode('raw_unicode_escape')  # cityName: Unicode
    cityId = city['cityid']
    cityName_cityID[cityName] = cityId

# 县级市处理
with open('meizu_country.json', 'r') as m:
    data_country = m.read().decode('gbk').encode('utf-8')
    city_country = json.loads(data_country)
    cityList_country = city_country["countries"]
for country in cityList_country:
    CountryName = country['countyname'].encode('raw_unicode_escape')
    CountryId = country['areaid']
    cityName_cityID[CountryName] = CountryId


def cityname_transfer_cityid(cityname):
    """
    输入城市名称，输出为城市对应的ID
    :param cityname:
    :return cityID
    """
    cityNameUnicode = cityname.decode('utf-8').encode('raw_unicode_escape')
    try:
       result_city_id = cityName_cityID[cityNameUnicode]
    except KeyError:
        print "输入城市错误,请重新输入(enter 'q' to exit)："
        name = raw_input()
        if name == 'q':
            os._exit(1)
        return cityname_transfer_cityid(name)
    else:
        return result_city_id

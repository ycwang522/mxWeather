# Python2.7 实现天气查询



> @version: Python 2.7
>
> API :  [魅族天气API ](http://aider.meizu.com/app/weather/listWeather?cityIds= )
>
> API使用方式：http://aider.meizu.com/app/weather/listWeather?cityIds= + 城市代码(比如，北京的代码为101010100)
>
> http://aider.meizu.com/app/weather/listWeather?cityIds=101010100 

</br>

## 文件说明



- *Weather.py*  主程序
- *meizu_city.json*  地级市——城市名称和城市ID的*json*格式的数据
- *meizu_country.json* 县级市——城市名称和城市ID的*json*格式数据
- *cityName_cityId.json*  由{城市名称：城市ID}构成的一个字典，从*meizu_city.json* 和 *meizu_country.json*中提取
- *cityName_transfer_cityID.py*  该文件对两个*json*数据文件进行整合。输入城市名称，返回对应城市的数字代码。


</br>

#### 重点说明一下最后一个文件 *cityName_transfer_cityID.py*

由于源数据文件*meizu_country.json* 和 *meizu_city.json* 中的数据格式是{"cityID": 101010100, "cityName": 北京 }这样的形式，Python中进行URL拼接时不能直接得到城市代码。

##### 采取的方法是：

新建一个*dict*，遍历两个数据文件并将*cityName*和*cityID*按照如下的格式存储：

> *dict[cityName] = cityID*

这样就可以通过访问字典来返回城市代码了。

##### 编码问题

上述方案有一个问题，就是通过*json*解析之后，中文在dict的存储变成了形如`\u8302\u6e2f`的形式，这种编码格式称为 *<u>usc2</u>*

> *\u5317\u4EAC*
>
> 对应“北京”

但是通常查询的时候直接输入城市的中文名更为直观，但是这样与dict中存储的地名肯定不匹配，也就无法返回对应的城市代码。因此需要进行编码格式的转换。

有两种转换方式

- 将*dict*中的所有*cityName*转换为中文
- 将输入的中文转换为如上*usc2*的编码格式

通过比较两种转换方式，第一种的转换更为繁琐，而且工作量更大，仅仅对输入进行转换再进行匹配的方案更好一些。

于是进行如下的转换：

```python
cityNameUnicode = cityname.decode('utf-8').encode('raw_unicode_escape')
# 將輸入按照'utf-8'解碼再重新編碼為'raw_Unicode_escape'格式
```

</br>

## 运行界面

输入城市名称(enter 'q' to exit):北京

| 日期                 | 天气     | 温度               |
| :----------------- | :----- | :--------------- |
| 日期: 2018-01-31 星期三 | 天气: 晴  | 温度: -8 ℃ ~ 4 ℃   |
| 日期: 2018-02-01 星期四 | 天气: 多云 | 温度: -7 ℃ ~ 4 ℃   |
| 日期: 2018-02-02 星期五 | 天气: 晴  | 温度: -10 ℃ ~ -1 ℃ |
| 日期: 2018-02-03 星期六 | 天气: 晴  | 温度: -10 ℃ ~ 0 ℃  |
| 日期: 2018-02-04 星期日 | 天气: 晴  | 温度: -8 ℃ ~ 1 ℃   |
| 日期: 2018-02-05 星期一 | 天气: 晴  | 温度: -9 ℃ ~ 2 ℃   |
| 日期: 2018-01-30 星期二 | 天气: 晴  | 温度: -7 ℃ ~ 5 ℃   |

</br>

![运行界面](http://imglf3.nosdn.127.net/img/ZG9uT3VOcDRVemdobW1VTmpNaXpDU3Y4TW9ncDhrQUZGRXBlZXFPclV5UXdxSGxVaXhlaTZ3PT0.bmp?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg)


## Done

Thanks：https://github.com/jokermonn/-Api
# coding:utf-8
import json



with open('mz.json', 'r') as json_file:
    file = json_file.read()
    print file.decode(encoding='gbk')

with open('meizu.json', 'r') as json_file1:
    data = json_file1.read().decode(encoding='gbk').encode(encoding='utf-8')
    print type(data)
    result = json.loads(data)
    new_result = json.dumps(result,ensure_ascii=False)
    print new_result
    print type(result)
    print result["cities"]


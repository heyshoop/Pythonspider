# -*-coding:utf8-*-
import datetime
import time
import requests
import json

#生成随机数
def datetime_to_timestamp_in_milliseconds(d):
    current_milli_time = lambda: int(round(time.time() * 1000))
    return current_milli_time()
#设置头部
head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/873981/',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
#要爬取的连接
urls = []

for i in range(1, 2):
    url = 'http://space.bilibili.com/ajax/member/GetInfo?mid=' + str(i)
    urls.append(url)

payload = {
        '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
        'mid': url.replace('http://space.bilibili.com/ajax/member/GetInfo?mid=', '')
    }

print(payload)
jscontent = requests.post('http://space.bilibili.com/ajax/member/GetInfo', headers=head,  data=payload).content
print(jscontent)

jsDict = json.loads(jscontent.decode())

print(jsDict)
if jsDict['status'] == True:
    print(jsDict['data']['name'])

#用爬虫从有道进行翻译
import urllib.request
import urllib.parse
import json
import time

while True:

    content = input('清输入需要翻译的内容(输入q退出程序)：')
    if content == 'q':
        break
    
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    """
    错误示范
    url = http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    """

    header = {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'}


    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to']= 'AUTO'
    data['smartresult']= 'dict'
    data['client']= 'fanyideskweb'
    data['salt']= '16002637458347'
    data['sign']= '0da3fd1c6d0fcd0898f766b020ca6869'
    data['lts']= '1600263745834'
    data['bv']= '1e0e7e419bda4ef6ac3b97fbcc0153eb'
    data['doctype']= 'json'
    data['version']= '2.1'
    data['keyfrom']= 'fanyi.web'
    data['action']= 'FY_BY_REALTlME'

    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']
    print(target)
    time.sleep(2)  #延迟2s




    #将在审查元素中获得的url中translate后面的_o去掉，错误就消失了，可以正常爬取。

    #data除了doctype键和i键不能去掉，其余的即使删除了也能正常运行翻译。[此行待验证]

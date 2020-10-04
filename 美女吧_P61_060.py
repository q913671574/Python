import urllib.request
import re
from bs4 import BeautifulSoup

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html


def get_img(html):
    p = r'bpic=\"(.*?)\"'
    imglist = re.findall(p, str(html))
    picnum = 0
    for each in imglist:
        print(each)
        if (".jpg" in each):
            with open(str(picnum) + ".jpg", 'wb') as f:
                img = urllib.request.urlopen(each, timeout = 3).read()
                f.write(img)
                picnum += 1
                f.close()

    print('down')
    



if __name__ == '__main__':
    url = 'https://tieba.baidu.com/f?kw=%C5%AE%C9%F1&fr=ala0&tpl=5'
    get_img(open_url(url))

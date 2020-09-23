import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    print(url)
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('')
    b = html.find(a)

    return html[a:b]

def find_img(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
            
        a = html.find('img src=', b)

        for each in img_addrs:
            print(each)

def save_imgs(folder, img_addrs):
    for each in img.addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)
def download_mm(folder = 'ooxx', pages = 10):
    os.mkdir(floder)
    os.chdir(floder)

    url = 'https://www.tupianzj.com/meinv/mm/meizitu/'
    pagenum = int(get_page(url))
    for i in 
    

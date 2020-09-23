import urllib.request

url = 'http://www.whatismuip.com.tw'    #访问此网站将返回自己的IP地址

#设置代理
proxy_support = urllib.request.ProxyHandler({'http':'122.72.99.8:80'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
opener.addheader = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400')]

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)

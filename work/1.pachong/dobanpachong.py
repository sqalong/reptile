import requests
from lxml import etree

def zhu():
    #定义请求的参数
    urls = ['https://movie.douban.com/top250?start='+str(i)+'&filter=' for i in range(0,226,25)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36'
    }
    for url in urls:
        print(url)
        re = requests.get(url,headers=headers)
        # print(re.text)
        ye = etree.HTML(re.text)
        # print(ye)
        infos = ye.xpath('//div[@id="wrapper"]//ol[1]/li')
        for info in infos:
            name = info.xpath('.//div/div[2]/div[1]/a/span[1]/text()')
            print(name)


zhu()
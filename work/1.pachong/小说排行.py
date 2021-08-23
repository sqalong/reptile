import csv
from lxml import etree
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'' (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
# csvv = open('xss.csv', 'w+', newline='', encoding='utf-8-sig')
# writer = csv.writer(csvv)
# writer.writerow(('排名', '书名', '作者', '字数', '点击量', '更新时间'))
urls = ['http://top.hengyan.com/dianji/default.aspx?p={}'.format(str(i)) for i in range(1, 10, 1)]
for url in urls:
    rex = requests.get(url)
    print(url)
    yiem = etree.HTML(rex.text)
    print(yiem)
    infos = yiem.xpath('//div[@class="list"]//ul')
    print(infos)
    for info in infos:
        num = info.xpath('li[@class="num"]/text()')[0]
        author = info.xpath('li[@class="author"]/text()')[0]
        length = info.xpath('li[@class="length"]/text()')[0]
        click = info.xpath('li[@class="length"]/text()')[0]
        update = info.xpath('li[@class="update"]/text()')[0]
        link = info.xpath('li[@class="bookname"]/a[1]/@href')
        # writer.writerow(())
        print((num,author, length, click, update,link))
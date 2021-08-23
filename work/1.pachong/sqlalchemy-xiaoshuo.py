from lxml import etree
import requests
from sqlalchemy import create_engine
connect = create_engine('mysql+pymysql://root:123456@192.168.100.142:3306/bo',encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'' (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
urls = ['http://top.hengyan.com/dianji/default.aspx?p={}'.format(str(i)) for i in range(1, 10, 1)]
for url in urls:
    rex = requests.get(url)
    yiem = etree.HTML(rex.text)
    infos = yiem.xpath('//div[@class="list"]//ul')
    for info in infos:
        num = info.xpath('li[@class="num"]/text()')[0]
        author = info.xpath('li[@class="author"]/text()')[0]
        length = info.xpath('li[@class="length"]/text()')[0]
        click = info.xpath('li[@class="length"]/text()')[0]
        update = info.xpath('li[@class="update"]/text()')[0]
        print(num,author,click, update)
        ee = connect.execute('insert into xiaoshuo values("%s","%s","%s","%s")' %(num,author,click, update))
        # print(ee)

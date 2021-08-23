
import pymysql
import requests
from lxml import etree

def zhu():
    # db = pymysql.connect(host="localhost", port=3306, user="root",
    #                      password="123456", db="bo", charset="utf8")
    # # cursor = db.cursor()
    # urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 251, 25)]
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    # }
    # for url in urls:
    #     re = requests.get(url, headers=headers)
    #     print(url)
    #     # print(re.text)
    #     ye = etree.HTML(re.text)
    #     # print(ye)
    #     # name = ye.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()')
    #     # print(name)
    #     infos = ye.xpath('//div[@id="wrapper"]//ol[1]/li')
    #     for info in infos:
    #         #     # yanyuan = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].strip().split('\xa0')[-1].split(':')[-1]
    #         num = info.xpath('.//div[@class="pic"]/em/text()')[0]
    #         name = info.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
    #         #     # daoyan = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].split('\xa0')[0].split(':')[1].strip()
    #         #     # guojia = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().replace('\xa0','').split('\n')[1].split('/')[1].split()[0]
    #         pingfen = info.xpath('.//div[@class="star"]/span[2]/text()')[0]
    #         pingjiarenshu = info.xpath('.//div[@class="star"]/span[4]/text()')[0]
    #         mingju = info.xpath('.//div[@class="bd"]//p//span/text()')
    #         # print(num)
    #         # print(mingju)
    #         if not mingju:
    #             mingju = "无"
    #         mingju = mingju[0]
    #         # print(num,name,pingfen,pingjiarenshu,mingju)
    #         # sql = 'insert into doub values ("%s","%s","%s","%s","%s","%s","%s","%s")' % (num,name,daoyan,yanyuan,guojia,pingfen,pingjiarenshu,mingju)
    #         # cursor.execute(sql)
    #         # db.commit()
 info="[2021-08-10 19:35:24][__init__.py:publish_data:128][INFO]->push the data [团结里_新征里_双_累积电量] -> [ns=2;i=444]: 22412.609375[2021-08-10 19:35:24][__init__.py:publish_data:128][INFO]->push the data [团结里_昌德城_双_累积电量] -> [ns=2;i=445]: 13528.3095703125"
 yanyuan = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].strip().split('\xa0')[-1].split(':')[-1]
zhu()

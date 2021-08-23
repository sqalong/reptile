import csv

import pymysql
import requests
from lxml import etree


def zhu():
    # db = pymysql.connect(host="192.168.100.142", port=3306, user="root",
    #                      password="123456", db="bo", charset="utf8mb4")
    # cursor = db.cursor()
    urls = ["https://www.aboutyun.com/forum-148-" + str(i) + ".html" for i in range(1, 7, 1)]
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    for url in urls:
        re = requests.get(url, headers=header)
        ye = etree.HTML(re.text)
        infos = ye.xpath('.//*[@id="threadlisttableid"]/tbody')
        for info in infos:
            leixing = info.xpath('.//tr/th/em/a/text()')
            name = info.xpath('.//tr/th/a[3]/text()')
            dizhi = info.xpath('.//tr/th/a/@href')
            if not dizhi:
                dizhi = 'wu'
            else:
                dizhi = dizhi[-1]
            huifu = info.xpath('.//tr/td[3]/em/text()')
            print(leixing, name, dizhi, huifu)
            # sql = 'insert into w values ("%s","%s","%s","%s")' % (leixing,name,dizhi,huifu)
            # cursor.execute(sql)
            # db.commit()


zhu()

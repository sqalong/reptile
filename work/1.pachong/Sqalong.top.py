import pymysql
import requests
from lxml import etree

def zhu():
    # db = pymysql.connect(host="", port=3306, user="root",
    #                      password="123456", db="bo", charset="utf8")
    # cursor = db.cursor()
    # csvv = open('E://爬虫数据/豆瓣排行数据+演员.csv', 'w+', newline='', encoding='utf-8-sig')
    # writer = csv.writer(csvv)
    # writer.writerow(('排名', '电影名称', '导演','演员','国家', '评分', '评价人数', '名句'))
    url = 'http://sqalong.top/index.jsp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    str = 0
    while True:
        re = requests.get(url, headers=headers)
        # print(re)
        ye = etree.HTML(re.text)


        # print(ye)
        # infos = ye.xpath('//div[@id="wrapper"]//ol[1]/li')
        # # print(infos)
        # for info in infos:
        #     yanyuan = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].strip().split('\xa0')[-1].split(':')[-1]
        #     # print(info)
        #     num = info.xpath('.//div[@class="pic"]/em/text()')[0]
        #     name = info.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
        #     daoyan = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].split('\xa0')[0].split(':')[1].strip()
        #     guojia = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().replace('\xa0','').split('\n')[1].split('/')[1].split()[0]
        #     pingfen = info.xpath('.//div[@class="star"]/span[2]/text()')[0]
        #     pingjiarenshu = info.xpath('.//div[@class="star"]/span[4]/text()')[0]
        #     mingju = info.xpath('.//div[@class="bd"]//p//span/text()')
        #     if not mingju:
        #         mingju = "无"
        #     mingju = mingju[0]
        #     print('序号'+num+"\n"+'电影名'+name+"\n"+daoyan,yanyuan,guojia,pingfen,pingjiarenshu,mingju)
        #     # sql = 'insert into doub values ("%s","%s","%s","%s","%s","%s","%s","%s")' % (num,name,daoyan,yanyuan,guojia,pingfen,pingjiarenshu,mingju)
        #     # cursor.execute(sql)
        #     # db.commit()
        #     # writer.writerow((num,name,daoyan,yanyuan,guojia,pingfen,pingjiarenshu,mingju))


zhu()

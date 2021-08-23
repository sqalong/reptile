import csv
from lxml import etree
import requests
import pymysql

def zhu():
    connect = pymysql.connect('localhost','root','123456','q',charset='utf8')
    cur = connect.cursor()
    csvv = open('szlj.csv','w+',encoding='utf-8-sig',newline='')
    writer = csv.writer(csvv)
    q={}
    q['tianjin'] = "tj"
    q['shanghai'] = "sh"
    q['guangzhou'] = "gz"
    q['shenzheng'] = "sz"
    urls = ['https://'
            +e+
            '.fang.lianjia.com/loupan/pg'+str(i)
            for e in q.values()for i in range(1,71,1)
            ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    for url in urls:
        re = requests.get(url, headers=headers)
        ye = etree.HTML(re.text)
        infos = ye.xpath('.//div[4]/ul[2]/li')
        for info in infos:
            name = info.xpath('./div[1]/div[1]/a/text()')[0]
            fangxing = info.xpath('./div[1]/div[1]/span[1]/text()')[0]
            chengshis = info.xpath('./div[1]/div[2]//span[1]/text()')
            chengshi = "".join(chengshis)
            xiang = info.xpath('./div[1]/div[2]/a/text()')[0]
            mianji  = info.xpath('./div[1]/div[3]/span/text()')
            if not mianji:
                mianji = ''
            else:
                mianji = mianji[0].split()[1]
            hangjia = info.xpath('./div[1]/div[6]/div[1]/span[1]/text()')[0]
            # print(name,fangxing,chengshi,xiang,mianji,hangjia,)
            writer.writerow((name,fangxing,chengshi,xiang,mianji,hangjia,))
            sql = 'insert into lianjia values("%s","%s","%s","%s","%s","%s")' %(name,fangxing,chengshi,xiang,mianji,hangjia,)
            cur.execute(sql)
            connect.commit()


zhu()
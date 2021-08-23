import csv
import requests
from lxml import etree

def zhu():
    csvv = open('E://a爬虫数据/赶集网.csv', 'w+', newline='',encoding='utf-8,')
    writer = csv.writer(csvv)
    q = {}
    q['beijijng']="bj"
    q['shanghai']="sh"
    q['guangzhou']="gz"
    q['shenzhen']="sz"
    q['wuahn']="wh"
    q['tianjing']="tj"
    q['nanjing']="nj"
    q['hangzhou']="hz"
    urls=['http://'
          +w+
          '.ganji.com/zufang/pn'
          +str(i)+
          '/'for w in q.values()for i in range(1,70,1)
          ]
    header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36'}
    for url in urls:
        # print(url)
        re = requests.get(url,headers=header)
        ye = etree.HTML(re.text)
        infos = ye.xpath('.//div[6]/div[1]/div[3]/div[1]/div[@class="f-list-item ershoufang-list"]')
        # print(infos)
        for info in infos:
            chengshi = ye.xpath('//*[@id="header"]/div/div[1]/a[1]/text()')[0]
            didian = info.xpath('./dl/dd[3]/span/a[1]/text()')[0]
            name = info.xpath('./dl/dd[1]/a/text()')[0]
            jiaqian= info.xpath('./dl/dd[@class="dd-item info"]/div[1]/span[1]/text()')[0]
            pingmi = info.xpath('./dl/dd[2]/span[3]/text()')[0][:-1]
            print(chengshi,didian,name,jiaqian,pingmi)
            writer.writerow((chengshi,didian,name,jiaqian,pingmi))

zhu()

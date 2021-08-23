import csv
from lxml import etree
import requests

def zhu():
    # csvv = open('E:\爬虫数据\szlj.csv','w+',encoding='utf-8-sig',newline='')
    # writer = csv.writer(csvv)
    q = {}
    q['beijin'] = "bj"
    q['shanghai'] = "sh"
    q['guangzhou'] = "gz"
    q['shenzheng'] = "sz"
    urls = ['http://'
            +w+
            '.ganji.com/zufang/pn'+str(i)+'/'
            for w in q.values() for i in range(1,71,1)
            ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    for url in urls:
        # print(url)
        re = requests.get(url, headers=headers)
        ye = etree.HTML(re.text)
        infos = ye.xpath('//*[@id="f_mew_list"]/div[6]/div[1]/div[3]/div/div[2]')
        print(infos)
        for info in infos:
            name = info.xpath('./div[1]/div[1]/a/text()')
            fangxing = info.xpath('./div[1]/div[1]/span[1]/text()')
            chengshis = info.xpath('./div[1]/div[2]//span[1]/text()')
            chengshi = "".join(chengshis)
            xiang = info.xpath('./div[1]/div[2]/a/text()')
            mianji  = info.xpath('./div[1]/div[3]/span/text()')
            if not mianji:
                mianji = ''
            else:
                mianji = mianji[0].split()[1]
            hangjia = info.xpath('./div[1]/div[6]/div[1]/span[1]/text()')
            print(name,fangxing,chengshi,xiang,mianji,hangjia,)
            # writer.writerow((name,fangxing,chengshi,xiang,mianji,hangjia,))



zhu()
import csv
import requests
from lxml import etree
def zhu():
    w = {}
    w ['beijian']='010000'
    w['shanghai']='020000'
    w['guangzhou']='030200'
    w['shenzheb']='040000'
    w['wuhan']='180200'
    w['xian']='200200'
    urls = ["https://search.51job.com/list/"
            +q+
            ",000000,0100%252C2600%252C2700,01,9,99,%2520,2,"
            +str(i)+
            ".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
            for q in w.values() for i in range(1, 21, 1)]
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    for url in urls:
        # print(url)
        re = requests.get(url=url,headers=header)
        re.encoding = 'gbk'
        ye = etree.HTML(re.text)
        infos = ye.xpath('//*[@id="resultList"]/div[@class="el"]')
        # print(info)
        for info in infos:
            name = info.xpath('./p/span/a/@title')
            if not name:
                name = ''
            else:
                name = name[0]
            gongsi = info.xpath('./span[1]/a/@title')
            if not gongsi:
                gongsi = ''
            else:
                gongsi = gongsi[0]
            dizhi = info.xpath('./span[2]/text()')
            if not dizhi:
                dizhi = ''
            else:
                dizhi = dizhi[0].split('-')[0]
            if dizhi == '异地招聘':
                dizhi = ''
            yuexin = info.xpath('.//span[3]/text()')
            if not yuexin:
                yuexin = ''
            else:
                yuexin = yuexin[0].split('-')[0]
            shijian = info.xpath('.//span[4]/text()')
            if not shijian:
                shijian = ''
            else:
                shijian = shijian[0]
            print(name,)

zhu()
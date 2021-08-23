import csv
from lxml import etree
import requests
def zhu():
    csvv = open('taobao.csv','w+',encoding='utf-8')
    writer = csv.writer(csvv)

    urls={"https://re.taobao.com/search_ou?spm=a231k.13731936.21333857.202.1bcb2e63NQNoHS&prepvid=300_11.224.246.224_12726_1575015655348&extra=&keyword=%E6%83%85%E8%B6%A3%E7%94%A8%E5%93%81&catid=&refpid=mm_26632258_3504122_32538762&_input_charset=utf8&clk1=79034920d4ff25b966075ced7e858579&page="+str(i)+"&rewriteKeyword=%E6%83%85%E8%B6%A3%E7%A0%94%E4%B9%A0%E7%A4%BE"for i in range(1,99,1)}
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    for url in urls:
        re=requests.get(url,headers=headers)
        ye=etree.HTML(re.text)
        infos=ye.xpath('/html/body/div[2]//div[1]/div[@id="J_waterfallWrapper"]/div')
        for info in infos:
            name = info.xpath('.//a/div[2]/span/text()')
            if not name:
                name = ''
            else:name = name[0]
            jiaqian = info.xpath('.//a/div[2]/p[1]/span[1]/strong/text()')
            if not jiaqian:
                jiaqian = ''
            else:jiaqian = jiaqian[0]
            dianpu = info.xpath('.//a/div[2]/p[2]/span[1]/text()')
            if not dianpu:
                dianpu = ''
            else:dianpu = dianpu[0]
            pingfen = info.xpath('.//a/div[2]/div/div/span/span[2]/text()')
            if not pingfen:
                pingfen=''
            else:pingfen=pingfen[0]
            fukuan=info.xpath('./a/div[2]/p[2]/span[2]/text()')
            if not fukuan:
                fukuan=''
            else:fukuan=fukuan[0]
            print(name,jiaqian,dianpu,pingfen,fukuan)
            writer.writerow((name,jiaqian,dianpu,pingfen,fukuan))

zhu()
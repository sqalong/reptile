import csv
import requests
from lxml import etree

def zhu():
    csvv = open('jiudian.csv','w',newline='',encoding='utf-8-sig')
    writer = csv.writer(csvv)
    writer.writerow(('酒店名称','位置','房型','评分','好评率','特点'))
    urls = ['https://hotels.ctrip.com/hotel/beijing1/p{}'.format((str(i)))for i in range(1,21,1)]
    print(urls
          )
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    for url in urls:
        re = requests.get(url,headers=headers)
        ye = etree.HTML(re.text)
        # print(ye)
        infos = ye.xpath('.//div[@class="base_wrap3 "]/div[@class="base_main3"]/div[@id="hotel_list"]/div[@class="hotel_new_list J_HotelListBaseCell"]')
        # print(infos)
        for info in infos:
            name = info.xpath('.//li[1]//a/@title')[0]
            weizhis = info.xpath('.//li[2]/p[1]/a/@title')
            weizhi = "".join(weizhis)
            fangxing = info.xpath('.//li[2]//span[3]/@title')
            if not fangxing:
                fangxing = "无"
            pingfen = info.xpath('.//li[4]//div[1]/a//span[@class="hotel_value"]/text()')
            if not pingfen:
                pingfen = '无'
            tuijian = info.xpath('.//li[4]//div[1]/a//span[@class="total_judgement_score"]/span/text()')[0]
            tedians = info.xpath('.//li[4]//div[1]/a//span[@class="recommend"]/text()')
            if not tedians:
                tedian = "无"
            else:
                tedian = "".join(tedians)
            # jiaqian = info.xpath('.//li[3]/div[@class="J_Price_6410223"]')
            # jiaqian = info.xpath('//div[@class="hotel_price"]//span/text()')
            # jiaqian = info.xpath('./ul//li[3]//div[1]/div/a/span/text()')
            fangxing = fangxing[0]
            pingfen = pingfen[0]
            print(name,weizhi,fangxing,pingfen,tuijian,tedian)
            writer.writerow((name+',',weizhi+',',fangxing+',',pingfen+',',tuijian+',',tedian))



zhu()









import csv
import requests
from lxml import etree
myheaders = {
   'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

citycode = {}
citycode["beijing"] = "beijing1"
citycode["shanghai"] = "shanghai2"
citycode["tianjin"] = "tianjin3"
citycode["chongqing"] = "chongqing4"
csvv = open('jiudian.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(csvv)
writer.writerow(('酒店名称','位置','房型','评分','好评率','特点'))
writer = csv.writer(csvv, delimiter=',')

'''四个城市，十页数据的地址'''
allUrl=["https://hotels.ctrip.com/hotel/beijing"+str(city)+"p"+str(page) for page in range (1,10,1) for city in range(1,4,1)]
print(allUrl)
'''获取详细链接'''
def read_page_link(urls):
    '''建立列表存放详情页'''

    '''循环每个url'''
    for url in urls:
        re = requests.get(url, headers=myheaders)
        ye = etree.HTML(re.text)
        # print(ye)
        infos = ye.xpath(
            './/div[@class="base_wrap3 "]/div[@class="base_main3"]/div[@id="hotel_list"]/div[@class="hotel_new_list J_HotelListBaseCell"]')
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
            tuijians = info.xpath('.//li[4]//div[1]/a//span[@class="total_judgement_score"]/span/text()')
            if not tuijians:
                tuijian = "无"
            else:
                tuijian = "".join(tuijians)
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
            print(name, weizhi, fangxing, pingfen, tuijian, str(tedian))
            writer.writerow((name, weizhi, fangxing, pingfen,tuijian, tedian))
read_page_link(allUrl)

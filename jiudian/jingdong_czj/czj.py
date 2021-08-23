import csv
import urllib

import requests
from lxml import etree
import json

myheaders = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

csvv = open('D:\czj.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csvv)
writer.writerow(('酒店名称', '位置', '房型', '评分', '好评率', '特点'))
writer = csv.writer(csvv, delimiter=',')

url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=7224898&score=0&sortType=5&page=4&pageSize=10&isShadowSku=0&rid=0&fold=1"
print(url)
re = urllib.request.urlopen(url)
ww = json.loads(re.read())
print(ww)


import pprint

import requests
import json
import csv
from lxml import etree

# csvv =open('E://爬虫数据/某东女用杜蕾斯震动棒评论.csv', 'a', newline='')
# writer = csv.writer(csvv)
url = 'https://sclub.jd.com/comment/productPageComments.action?callback'
for i in range(20):
    page = i
    params = {
        'productId': 893780,
        'score': 0,
        'sortType': 5,
        'page': i,
        'pageSize': 10,
    }
    headers = {
        'cookie': '__jdu=1115472958; areaId=5; shshshfpa=c89ba6b3-6bd8-ef72-e2d8-016478dd5dc0-1575967151; shshshfpb=onE1oFCPobm5s6mDExunlcA%3D%3D; user-key=61c4388c-f894-400c-ae19-05eacf6c582c; cn=0; ipLoc-djd=5-142-143-5008; unpl=V2_ZzNtbUtVRRxzCkEGL0tdDGJRQlwSUUJFcwtEVH5KWlc1ARdeclRCFX0URldnGVQUZwoZWUpcQRdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsZXAFiBRFVRl5zJXI4dmRyHVoAZgUiXHJWc1chVEZccx1dByoDEl1GUkUWfQxPZHopXw%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_8378736cec084ca0a70a72314b7cc342|1576753174140; PCSYCityID=CN_130000_130400_130431; __jda=122270672.1115472958.1575967148.1575967198.1576753174.4; __jdc=122270672; 3AB9D23F7A4B3C9B=ZBRFUY5SPO7TXUVHE3PJTNWECZU2CQRNQBLQDSRBIKCZRNSM4FCDNPZ3J3ZSV3ZSP2TZ5GAYHILFDXDVJYIGN2HFIY; shshshfp=46fafadc2a0602adba0423e2c489ebc2; JSESSIONID=B8815F79E2A0A6DD25FF89753C1C45F5.s1; shshshsID=893ac2a21c2240219329f7fc28ba4c81_6_1576753438209; __jdb=122270672.7.1115472958|4.1576753174',
        'referer': 'https://item.jd.com/893780.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36'
    }
    re = requests.get(url=url, params=params, headers=headers).text
    re_dict = json.loads(re)
    print(re_dict)
    comments = re_dict['comments']
    print(type(comments))
    for comment in comments:
        user = comment['content']
        print(user)
        color = comment['creationTime']
        print(color)
        # writer.writerow((user,color))


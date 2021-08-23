#coding=utf-8
#今日头条
from lxml import etree
import requests
import urllib

def get_url():
    url = 'https://www.toutiao.com/ch/news_hot/'
    headers = {
    'Host': 'www.toutiao.com',
     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
     'Connection': 'Keep-Alive',
    'Content-Type': 'text/plain; Charset=UTF-8',
    'Accept': '*/*',
    'Accept-Language': 'zh-cn',
     'cookie':'__tasessionId=u690hhtp21501983729114;cp=59861769FA4FFE1'}
    response = requests.get(url,headers = headers).json()
    print (response)
    # html = response.content
    #  #print html
    # tree = etree.HTML(html)
    # title = tree.xpath('//a[@class="link title"]/text()')
    # source = tree.xpath('//a[@class="lbtn source"]/text()')
    # comment = tree.xpath('//a[@class="lbtn comment"]/text()')
    # time = tree.xpath('//span[@class="lbtn"]/text()')
    # print (len(title))   #0
    # print (type(title))  #<type 'list'>
    # for x,y,z,q in zip(title,source,comment):
    #     count += 1
    #     data = {
    #         'title':x.text,
    #         'source':y.text,
    #         'comment':z.text,
    #         'stime':q.text}
    #     # print(count,'|',data)
    #
    #

if __name__ == '__main__':
    count = 0
    get_url()
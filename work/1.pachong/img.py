import requests
from lxml import etree



url = "https://colorhub.me"#爬取的网站链接
header = {"user-agent":"Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"}#头部伪装信息
req = requests.get(url,headers=header)

print(req.status_code)#打印响应码，显示是否成功连接
html = etree.HTML(req.text)#把爬取下来的html变为lxml类型

arr=[]#定义空数组，用来存储标题
arr2 = []#定义数组，用来存储图片链接
print('++++++++++++++++++++++++++++++++++')
arr2=html.xpath('//div[contains(@class,"card")]//img/@src')
arr = html.xpath('//div[contains(@class,"card")]//img/@title')
print(arr)
print(arr2)
for i,j in zip(arr,arr2):#同时遍历两个数组
                        # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
                        #在Python3.x中为了减少内存，zip()返回的是一个对象。如需展示列表，需手动list()转换。
    jj = 'https:'+j#把图片链接补全
    with open(i+'.jpg','wb') as imgs:#用循环把图片写进图片文件
        jjs = requests.get(jj).content #再次用reqsts爬取图片链接的同时把图片变为二进制格式
        # print(jjs)
        imgs.write(jjs)#把图片的二进制写入图片文件
    print(i+jj)
    print('\n')#提示每张图片下载状态
    print('@@@@@@@@@@@'+i+'图片已经下载成功@@@@@@@@@@@@')#
    print('\n')
print('\t\t##########全部图片下载成功############')  
import requests
from lxml import etree

j=0
def zong():
    r=requests.get('http://new031.top/?m=vod-type-id-4-pg-'+i+'.html'for i in range(1,2,1)).content
    books=etree.HTML(r)
    imgs=books.xpath('//*[@id="subject_list"]/ul/li/div[1]/a/img/@src', stream=True)
    for img in imgs:
        j=j+1
        with open(str(j)+'.jpg', 'wb') as fd:
            picture=requests.get(img).content
            fd.write(picture)

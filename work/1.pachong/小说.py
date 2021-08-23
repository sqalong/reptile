# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import sys
#二九 小说网  逆天邪神



class downloader(object):
    

    def __init__(self):
        self.server = 'https://www.2952.cc'
        self.target = 'https://www.2952.cc/b/4/4712/index.html'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数

    def get_contents(self,target):
        req.encoding = req.apparent_encoding
        bf = BeautifulSoup(req.text,"html.parser")
        texts = bf.find_all('div',id="content")
        return (texts[0].text)

    def get_download_url(self):
       

        req = requests.get(url=self.target)
        req.encoding = req.apparent_encoding
        bf = BeautifulSoup(req.text,"html.parser")
        texts = bf.find_all('div',class_="dirtitone")
        div = BeautifulSoup(str(texts[0]),"html.parser")
        a = div.find_all('a')
        for each in a[1629:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def writer(self,name,path,text):
        writer_flag = True
        with open(path,'a',encoding = 'utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__=="__main__":

    d = downloader()
    start = time.perf_counter()
    d.get_download_url()
    print('《逆天邪神》开始下载：')
    for i in range(d.nums):
        d.writer(d.names[i], '逆天邪神.txt', d.get_contents(d.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / d.nums) + '\r')
        sys.stdout.flush()
print('《逆天邪神》下载完成,用时{:.5f}'.format((time.perf_counter()-start)))

import requests
from lxml import etree
import csv
class zhu():
    def qingwiu(self):
        self.urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 251, 25)]
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
        return
    def urlxunhuan(self):
        for url in self.urls:
            re = requests.get(url, headers=self.headers)
            ye = etree.HTML(re.text)
            infos = ye.xpath('//div[@id="wrapper"]//ol[1]/li')
    def paqu(self):
        for info in self.infos:
            self.yanyuan = \
            info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].strip().split('\xa0')[
                -1].split(':')[-1]
            # print(info)
            self.num = info.xpath('.//div[@class="pic"]/em/text()')[0]
            self.name = info.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
            self.daoyan = \
            info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].split('\xa0')[0].split(
                ':')[1].strip()
            self.guojia = \
            info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().replace('\xa0', '').split('\n')[1].split(
                '/')[1].split()[0]
            self.pingfen = info.xpath('.//div[@class="star"]/span[2]/text()')[0]
            self.pingjiarenshu = info.xpath('.//div[@class="star"]/span[4]/text()')[0]
            self.mingju = info.xpath('.//div[@class="bd"]//p//span/text()')
            if not mingju:
                mingju = "无"
            mingju = mingju[0]
    def chucun(self):
        csvv = open('E://爬虫数据/doubanclass.txt','w+',encoding='utf-8')
        writer = csv.writer(csvv)
        writer.writerow((self.num,self.name,self.daoyan,self.yanyuan,self.guojia,self.pingfen,self.pingjiarenshu,self.mingju))
        print(self.num,self.name,self.daoyan,self.yanyuan,self.guojia,self.pingfen,self.pingjiarenshu,self.mingju)
if __name__ == '__main__':
    zhu.qingwiu()
    zhu.urlxunhuan()

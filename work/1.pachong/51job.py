import csv
import requests
from lxml import etree

def zhu():
    # csvv = open('E://a爬虫数据/ee.csv', 'w+',newline='',encoding='utf-8')
    # writer = csv.writer(csvv)
    # writer.writerow(('职位名','公司名','城市','月薪','发布时间'))
    q = {}
    q["beijing"] = "010000"
    q["shanghai"] = "020000"
    q["guangzhou"] = "030200"
    q["shenzhen"] = "040000"
    q["wuhan"] = "180200"
    q["xian"] = "200200"
    urls = [
        "https://search.51job.com/list/"
        + w +
        ",000000,0100%252C2600%252C2700,01,9,99,%2B,2,"
        + str(i) +
        ".html?lang=c&fromJs=1&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=%22%20+%20%2214&dibiaoid=0&address=&line=&specialaread00&from=&welfare="
        for w in q.values() for i in range(1, 21, 1)
    ]
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    for url in urls:
        # print(url)
        re = requests.get(url, headers=header)
        re.encoding = 'gbk'
        ye = etree.HTML(re.text)
        infos = ye.xpath('//*[@id="resultList"]/div[@class="el"]')
        for info in infos:
            name = info.xpath('./p/span/a/@title')
            if not name:
                name = ''
            else:
              name = name[0]
            gongsi = info.xpath('./span[1]/a/@title')
            if not gongsi:
                gongsi=''
            else:gongsi = gongsi[0]
            dizhi = info.xpath('./span[2]/text()')
            if not dizhi:
                dizhi = ''
            else:dizhi=dizhi[0].split('-')[0]
            if dizhi == '异地招聘':
                dizhi =''
            shijian = info.xpath('.//span[4]/text()')
            if not shijian:
                shijian = ''
            else:shijian = shijian[0]
            yuexins = info.xpath('.//span[3]/text()')
            if not yuexins:
                yuexin = ''
            else:
                yuexin = yuexins[0]
                if  '月' in yuexin:
                    yuexin= yuexin.split('/')[0]
                    if '万' in yuexin:
                        # print('******************************************************************************************************************天')
                        q,w = yuexin[:-1].split('-')
                        # print(q,w)
                        yuexin =(float(q)+float(w))/2
                        yuexin = format(yuexin,'.1f')
                    else:
                        q, w = yuexin[:-1].split('-')
                        yuexin = (float(q)+float(w))/2/10
                        yuexin = format(yuexin,'.1f')
                elif '年' in yuexin:
                    if '万以下' in yuexin:
                        yuexin = yuexin.split('/')[0][:-3]
                        yuexin = float(yuexin)/12
                    else:
                        yuexin = yuexin.split('/')[0][:-1]
                        q, w = yuexin.split('-')
                        yuexin = (float(q) + float(w)) / 2 / 12
                        yuexin = format(yuexin, '.1f')
                elif '天' in yuexin:
                    y = yuexin.split('/')[0][:-1]
                    yuexin = float(y)*30/10000
                    yuexin = format(yuexin, '.1f')

            print(name, gongsi, dizhi, yuexin, shijian)
            # writer.writerow((name, gongsi, dizhi, yuexin, shijian))
if __name__ == '__main__':
    zhu()
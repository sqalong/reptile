import requests
from bs4 import BeautifulSoup
import csv
myheaders = {
   'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

'''获取各页链接'''
allUrl = ['https://www.bilibili.com/v/kichiku/guide/?spm_id_from=333.5.b_6b696368696b755f6775696465.3#/all/default/0/{}'.format((str(page)))for page in range(1,20,1)]
print(allUrl)

'''获取详情页连接'''
def read_page_links(urls):
   moviedetialpages = []
   for url in urls:
      r = requests.get(url=url, headers=myheaders)
      soup = BeautifulSoup(r.content.decode(encoding='utf-8'), 'lxml')
      for divTag in soup.find_all('div', attrs={'id': "app"}):
         print(divTag.text)
         if divTag is not None:
            aTag = divTag.find('a')
            link = aTag['href']
            print(link)
            moviedetialpages.append(link)
   return moviedetialpages

joblinks = read_page_links(allUrl)
print(joblinks)
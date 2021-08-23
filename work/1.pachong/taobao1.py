# !/usr/bin/nev python
# -*-coding:utf8-*-

import time, os, csv, datetime
from selenium import webdriver


class TBSpider(object):
    def __init__(self):
        self.count = 1
        self.keyword = input(r'请输入要查询的淘宝商品信息名称：')
        self.file_name = self.keyword + datetime.datetime.now().strftime('%Y-%m-%d')
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\23694\AppData\Local\Programs\Python\Python36\chromedriver.exe')

    def create_dir(self):
        '''
            创建文件夹
        '''
        if not os.path.exists(r'./{}'.format('商品信息数据')):
            os.mkdir(r'./{}'.format('商品信息数据'))
        self.write_header()

    def write_header(self):
        '''
            写入csv头部信息
        '''
        if not os.path.exists(r'./{}.csv'.format(r'***商品数据保存成功：{}'.format(self.keyword))):
            csv_header = ['商品名称', '商品价格', '销量', '商品店铺', '商品链接']
            with open(r'./{}/{}.csv'.format('商品信息数据', self.file_name), 'w', newline='', encoding='gbk') as file_csv:
                csv_writer_header = csv.DictWriter(file_csv, csv_header)
                csv_writer_header.writeheader()
        self.request_start_url()

    def request_start_url(self):
        '''
            请求起始url
        '''
        self.driver.get('https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=&clk1=b563659abe93a96a4e4c136b8d38b209&upsId=b563659abe93a96a4e4c136b8d38b209&spm=a2e0b.20350158.31919782.1&pnum=0')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.search_goods()

    def search_goods(self):
        '''
            输入商品关键字
        '''
        print('\n' + r'----------------正在搜索商品信息：{}--------------------'.format(self.keyword) + '\n')
        self.driver.find_element_by_id('J_search_key').send_keys(self.keyword)
        self.driver.find_element_by_class_name('submit').click()
        time.sleep(3)
        self.mouse_scroll()

    def mouse_scroll(self):
        '''
            鼠标滑轮滚动，实现懒加载过程
        '''
        print(r'----------------正在请求第{}页数据--------------------'.format(self.count) + '\n')
        for i in range(1, 11):
            js = r'scrollTo(0, {})'.format(600 * i)
            # js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %s' % (i / 20)
            self.driver.execute_script(js)
            time.sleep(1)
        self.get_goods_info()

    def get_goods_info(self):
        '''
            解析得到商品信息字段
        '''
        li_list = self.driver.find_elements_by_xpath('//div[@class="lego-pc-search-list pc-search-list"]/ul')
        for li in li_list:
            name = li.find_elements_by_xpath(r'//li[@class="pc-items-item item-undefined"]/a/div['
                                             r'@class="pc-items-item-title pc-items-item-title-row2"]/span')

            price = li.find_elements_by_xpath(r'//li[@class="pc-items-item item-undefined"]/a/div['
                                              r'@class="price-con"]/span[2]')

            xiaoliang = li.find_elements_by_xpath(r'li[@class="pc-items-item item-undefined"]/a/div['
                                                  r'@class="item-footer"]/div[2]')
            vendor = li.find_elements_by_xpath(r'//*[@id="mx_5"]/ul/li/a/div[3]/div')
            link = li.find_elements_by_xpath(r'//li[@class="pc-items-item item-undefined"]/a')

            for a, b, c, d, e in zip(name, price, xiaoliang, vendor, link):
                f = a.text
                g = b.text
                h = c.text
                i = d.text.replace('', '')
                j = e.get_attribute('href')
                self.save_data(f, g, h, i, j)

    def save_data(self, name, price, xiaoliang, vendor, link):
        '''
            写入csv文件主体信息
        '''
        try:
            with open(r'./{}/{}.csv'.format('商品信息数据', self.file_name), 'a+', newline='', encoding='gbk') as file_csv:
                csv_writer = csv.writer(file_csv, delimiter=',')
                csv_writer.writerow([name, price, xiaoliang, vendor, link])
                print(r'***商品数据保存成功：{}'.format(name))
        except Exception as e:
            pass

    def get_next_page(self):
        '''
            实现循环请求
        '''
        time.sleep(4)
        for index in range(2, 101):
            print(r'----------------第{}页数据保存完成--------------------'.format(self.count) + '\n')
            time.sleep(4)
            self.count += 1
            if index <= 100:
                self.driver.find_element_by_xpath(r'//*[@id="J_pc-search-page-nav"]/span[3]').click()
                self.mouse_scroll()
            else:
                print('\n' + r'---------------所有商品数据保存完成------------------')
                break

    def main(self):
        '''
            实现主要逻辑
        '''
        self.create_dir()
        self.get_next_page()
        print('\n' + r'-------------文件保存成功------------------')


if __name__ == '__main__':
    tb = TBSpider()
    tb.main()

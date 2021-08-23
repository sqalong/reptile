# 思路如下：
# 1，抓取索引页。利用requests请求目标站点，得到索引网页的html代码
# 2，抓取详情页内容。解析索引网页的html代码，得到详情页的信息。
# 3，下载数据。将图片，标题，url下载到本地
# 4，开启循环和多线程。对多页内容进行遍历，开启多线程提高抓取速度


import requests
from urllib.parse import urlencode  # 这个很有用
from requests.exceptions import RequestException
import json
import re
from bs4 import BeautifulSoup
import os
from hashlib import md5
from multiprocessing import Pool

# 1，抓取索引页。利用requests请求目标站点，得到索引网页的html代码
def get_page_index(offset, keyword):
    # 请求参数，F12后选择headers中查看
    data = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': '0',
        'format': 'json',
        'keyword': '哈士奇',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'
              '&'
    }
    # urlencode()可以把字典类型转化url的请求参数，这个很有用小技巧
    # 需要加前缀from urllib.parse import  urlencode
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(
        data)
    # 没什么说的，抓取索引页源码 ，这里我们抓取的是json文件

    response = requests.get(url)
    print(response)
    # try:
    #     if response.status_code == 200:  # 判断是否响应状态是否正常
    #         return response.text
    #     return None
    # except RequestException:
    #     print("请求页面出错")
    #     return None


# 解析1中json的源码
def parse_page_index(html):
    print(html)
    # json.loads()用于将str类型的数据转成dict，因为json文件是str类型的，转化为dict容易提取
    data = json.loads(html)
    print(data)
    # 加个判断保证data字典里的key有‘data’这个属性，道理我们都懂，就是怕程序报错，不加也没问题，加的话代码美观，而且保证了程序的安全性
    # if data and 'data' in data.keys():
    #     # get() 函数返回指定键（key或者属性）的值
    #     # 把每个article_url（图集链接）提取出
    #     for item in data.get('data'):
    #         yield item.get('article_url')


# 2，抓取详情页内容。解析索引网页的html代码，得到详情页的信息。


# 从上面获得的图集链接下手，请求图集源码
def get_page_detail(url):
    # 这里加个一个头部文件，是因为今日头条有点狗，他判断了我请求的浏览器属性，不加user-agent冒充浏览器不让我请求源码
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    # 和第一个函数一样的步骤，请求源码（原始html格式）
    response = requests.get(url, headers=head)
    print(response)
    # try:
    #     if response.status_code == 200:
    #         return response.text
    #     return None
    # except RequestException:
    #     print("请求页面出错", url)
    #     return None


# 对上面的请求到的源码（原始html格式）进行解析
# 仔细观察，我们需要提取的图片url是藏在一个gallery的类似于字典的结构里（但是这里是str类型），我们提取到图片链接需要
# def parse_page_detail(html, url):
#     # 这里我们需要提取图集的标题
#     soup = BeautifulSoup(html, 'lxml')
#     # 直接用css选择器选择中title，返回一个列表，去列表中第一个元素，获取其中的文本
#     title = soup.select('title')[0].get_text()
#     print(title)
#     # 正则匹配获取图集类图片的url
#     images_pattern = re.compile(r'gallery: JSON.parse\(\"(.*?)\"\),', re.S)
#     # 因为一个图集只有一个gallery，所以用search能极大提高提取速度
#     result = re.search(images_pattern, html)
#     if result:  # 判断result内是否有结果，同上，养成良好代码习惯
#         # result.group(1)获取result里面第1个括号内的内容，若group(2)为获取result里面第1个括号内的内容，这里没第二个括号emmm，，如果0的话是返回全部匹配到的源码
#         data = result.group(1)
#         # 去除掉所有双斜杆
#         data = re.sub(r'\\', '', data)
#         # 将str转化为字典
#         data = json.loads(data)
#         # 同上，为了保险起见，加个判断确保内容存在
#         if data and "sub_images" in data.keys():
#             sub_images = data.get('sub_images')
#             # 迭代获取image的url
#             # 相当于
#             # for item in sub_images:
#             #     images= item.get("url")
#
#             images = [item.get("url") for item in sub_images]
#             # 提取图片并保持图片的标题，图集链接，图片的url
#             for image in images:
#                 download_image(image)
#             return {
#                 'title': title,
#                 'url': url,
#                 'image': images
#             }


# # 3，下载数据。将图片，标题，url下载到本地
# # 请求图片url的二进制源码，并将二进制（content）源码进行保存操作
# def download_image(url):
#     print("正在下载", url)
#     head = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
#     }
#
#     try:
#         response = requests.get(url, headers=head)
#         if response.status_code == 200:
#             # 为了避免重复调用多行代码，这里我们把下载操作进行封装
#             save_image(response.content)
#         return None
#
#
#     except RequestException:
#         print("请求图片出错", url)
#         return None


# # 下载图片操作
# def save_image(content):
#     # 小技巧：format通过 {} 和 : 来代替以前的 % 。很好玩的一个函数
#     file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(),
#                                      'jpg')  # 存储文件的路径，{0}是文件的路径，{1}是文件的名称，{2}文件的后缀
#     # 避免文件重复，判断文件是否存在，如果不存在，进行下载操作
#     if not os.path.exists(file_path):
#         with open(file_path, 'wb') as f:
#             f.write(content)
#             f.close()


# def main(offset):
#     html = get_page_index(offset, '街拍')  # offset是页数，街拍是索引词
#     # 迭代每个 offset的json，获取每个json的图集链接
#     for url in parse_page_index(html):
#         # 请求图集源码
#         html = get_page_detail(url)
#         if html:
#             # 获取图片链接并下载
#             parse_page_detail(html, url)




import requests
from lxml import etree
import pymysql

def zhu():
    # 定义数据库
    #host:地址    potr:端口     user:用户名    password:密码     db:数据库名     charset:编码
    # db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="douban", charset="utf8")
    # cursor = db.cursor() #创建游标
    #定义请求参数地址   range()第一个参数起始数 ,第二个结束数,加1,第三个每次增加数
    urls= ['https://movie.douban.com/top250?start='+str(i)+'&filter=' for i in range(0,226,25)]
    #伪装浏览器请求
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36'
    }
    for url in urls:                                        #循环地址
        # print(url)
        re = requests.get(url,headers=headers)              #requers.get方法请求
        ye = etree.HTML(re.text)                            #用lxml中的etree模块解析获取到的页面内容,
        infos = ye.xpath('//div[@id="wrapper"]//ol[1]/li')  #解析完就可以用xpath解析了,获取循环点,拿到列表
        for info in infos:                                  #循环列表
            #https://www.runoob.com/xpath/xpath-tutorial.html  --------xpath教程
            num = info.xpath('.//div/div[1]/em/text()')[0]                      #[0]是取列表索引
            # /text()取标签内容 /@title取标签title属性值 /@href取标签href属性值
            name = info.xpath('.//div/div[2]/div[1]/a/span[1]/text()')[0]
            pingfem = info.xpath('.//div/div[2]/div[2]/div/span[2]/text()')[0]
            mingju = info.xpath('.//div/div[2]/div[2]/p[2]/span/text()')        #如果为空需进行判断
            if not mingju:                                                      #如果为空
                mingju = "无"                                                   #则
            mingju = mingju[0]
            print(num,name,pingfem,pingfem,mingju)
            #定义sql语句
            # sql = 'insert into douban_data values ("%s","%s","%s","%s")' % (num,name,pingfem,mingju)
            # cursor.execute(sql)         #执行语句
            # db.commit()



zhu()

from sqlalchemy import create_engine

# 初始化数据库链接
connect = create_engine('mysql+pymysql://root:123456@192.168.100.142:3306/bo',echo=True,encoding='utf-8')
print(connect)

                                              #原生数据库操作方法
# 创建对象的基类：
cur=connect.execute("select * from flasks1")
# print(cur.rowcount) #输出查询到的数据数
so = cur.fetchall() #输出列表数据
# print(so)
toshow = {'keyset':[],'values':[]}
for au in so:
    toshow['keyset'].append(au['key'])
    toshow['values'].append(au['val'])
    # print(toshow)
# 插入，输出影响行数
resinsert=cur.execute("insert into tb_dong(namex,sex) values('%s','%s')"%("东小东xx","F")).rowcount
print(resinsert)
# 添加
cur = connect.execute('insert into flasks1 values("hai","3345")')
# print(cur)



from sqlalchemy import create_engine
from flask import Flask,render_template
app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/static')
@app.route('/')
def zong():
    # 创建对象的基类：
    connect = create_engine('mysql+pymysql://root:123456@192.168.100.142:3306/bo',echo=True,encoding='utf-8')
    cur=connect.execute("select * from flasks1")
    # print(cur.rowcount) #输出查询到的数据数
    so = cur.fetchall() #输出列表数据
    # print(so)
    toshow = {'keyset':[],'values':[]}
    for au in so:
        toshow['keyset'].append(au['key'])
        toshow['values'].append(au['val'])
        print(toshow)
    return render_template('',**toshow)
if __name__ == '__main__':
    app.run(port=5000)
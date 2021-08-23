from django.db.models import manager
from sqlalchemy import create_engine

from flask import Flask,render_template
manager = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/static')
@manager.route('/')
def zong():
    connect = create_engine('mysql+pymysql://root:123456@localhost:3306/bo',encoding='gbk')
    print(connect)
    cur = connect.execute('select * from flasks1')
    so = cur.fetchall()
    toshow = {'keyset':[],'values':[]}
    for au in so:
        toshow['keyset'].append(au['key'])
        toshow['values'].append(au['val'])
        print(toshow)
    return render_template('51zhu.html',**toshow)

if __name__ == '__main__':
    manager.run()(post=8888)
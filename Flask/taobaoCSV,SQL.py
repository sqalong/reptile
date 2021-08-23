from flask import render_template
import pymysql
from flask import Flask
app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')
@app.route('/')
def zong():
    connect = pymysql.connect(host='',user='',password='',db='',charset='',cursorclass=pymysql.cursors.DictCursor)
    cur = connect.cursor()
    cur.execute('select * from ')
    rs = cur.fetchall()
    print(rs)
    with open('/home/','r',encoding='utf-8') as file:
        line = file.readlines()
        thow = {'keyset':[],'values':[]}
        for qq in line:
            k,v=qq.strip().split('')
            thow['keyset'].append(k)
            thow['values'].append(v)
    return render_template('q.html',**thow)
if __name__ == '__main__':
    app.run(port=5000)
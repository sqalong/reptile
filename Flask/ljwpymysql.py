import pymysql
from flask import Flask, render_template
app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')
@app.route('/')
def zong():
    connect = pymysql.connect(host='192.168.100.142',user='root',password='123456',db='bo',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    cur = connect.cursor()
    cur.execute('select * from doub')
    rs = cur.fetchall()
    toshow = {'keyset': [], 'values': []}
    for ww in rs:
        toshow['keyset'].append(ww['keyset'])
        toshow['values'].append(ww['values'])
    # return render_template('q.html', **toshow)
    print(toshow)
zong()
# if __name__=='__main__':
#     app.run(port=5000)

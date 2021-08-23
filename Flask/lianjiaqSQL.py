from flask import Flask,render_template
import pymysql
app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/static')
@app.route('/')
def defs():
    connect = pymysql.connect('localhost','root','123456','q',cursorclass=pymysql.cursors.DictCursor)
    cur = connect.cursor()
    cur.execute('select * from tb_student')
    rs = cur.fetchall()
    thow = {'keyset':[],'values':[]}
    for ww in rs:
        thow['keyset'].append(ww['stu_name'])
        thow['values'].append(ww['stu_id'])
        print(thow)

defs()
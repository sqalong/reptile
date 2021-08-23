from flask import Flask,render_template
import pymysql
app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/static')
@app.route('/')
def zhu():
    connect = pymysql.connect('localhost','root','123456','q',cursorclass=pymysql.cursors.DictCursor)
    cur = connect.cursor()
    cur.execute('select * from kaoshi ')
    re = cur.fetchall()
    # print(re)
    toshow = {'keyset':[],'values':[]}
    for ww in re:
        # print(ww)
        toshow['keyset'].append(ww['t'])
        toshow['values'].append({'value':ww['a'],'name':ww['t']})
        print(toshow)
    return render_template('line.html',**toshow)
if __name__ == '__main__':
    app.run()
# zhu()


from flask import Flask,render_template
import pymysql

app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')

@app.route('/')
def defs():
    connect = pymysql.connect('localhost', 'root', '123456', 'q', charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)
    cur = connect.cursor()
    cur.execute('select * from tb_student')
    rs = cur.fetchall()
    toshow = {'keyset': [], 'values': []}
    for ww in rs:
        toshow['keyset'].append(ww['stu_name'])
        toshow['values'].append({'value': ww['stu_id'], 'name': ww['stu_name']})  # {'value':ww['stu_id'],'name':ww['stu_name']}        ww['stu_id']
        print(toshow)

    return render_template('pie.html', **toshow)


if __name__ == '__main__':
    app.run(port=5000)

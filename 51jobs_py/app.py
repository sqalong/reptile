# _*_ coding: utf-8 _*_
from flask import Flask
from flask import render_template
salarys = {
   '上海': 10870,
   '北京': 10921,
   '广州': 9064,
   '杭州': 9423,
   '武汉': 7901,
   '深圳': 10967}
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')


@app.route('/')
def hello_world():
   return r'''<strong>薪资统计结果</strong><br /><a href='/stat'>统计</a>'''


@app.route('/stat')
def hello_table():
   # result =get_result()
   toshow = {
      'keyset': str(list(salarys.keys())),
      'values': str(list(salarys.values()))
   }
   return render_template('stat.html', **toshow)


if __name__ == '__main__':
   app.run(host='localhost', port=5000, debug=True)
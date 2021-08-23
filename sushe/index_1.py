from mysql import connector
from sqlalchemy import create_engine

from flask import Flask,render_template
app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/static')
@app.route('/')
def zong():
    connect = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/sushe')
    # print(connect)
    cur = connect.execute('select * from admin')
    so = cur.fetchall()
    toshow = {'username':[],'password':[]}
    for au in so:
        toshow['username'].append(au['Username'])
        toshow['password'].append(au['Password'])
    print(toshow)
    return render_template('index.html', **toshow)
    # print("sss")
if __name__=='__main__':
    app.run(port=5000)
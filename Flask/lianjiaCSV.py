from flask import Flask,render_template
app = Flask(__name__,template_folder='templates',static_url_path='/static',static_folder='static')
@app.route('/')
def suo():
    with open('E://a爬虫数据/天津.txt','r',encoding='utf-8')as song:
        line = song.readlines()
        thow = {'keyset':[],'vlaues':[]}
        for zong in line:
            k,v,*_=zong.strip().split(',')
            thow['keyset'].append(k)
            thow['vlaues'].append(v)     #{'vlaue':v,'name':k}
    return render_template('q.html', **thow)
if __name__ == '__main__':
    app.run(port='5000')

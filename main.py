from flask import Flask, render_template, request, url_for
from flask_paginate import Pagination, get_page_args
from flask_mysqldb import MySQL
import prediction as pred

app=Flask(__name__, static_folder='static', template_folder='templates')
import headline as hd

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secret'
app.config['MYSQL_DB'] = 'liar_dataset'

mysql = MySQL(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home',methods=['POST','GET'])
def home():
	if request.method=='POST':
		msg1=request.form.get('Search')
		if msg1=="":
			return render_template('index.html')
		msg,prob=pred.detecting_fake_news(msg1)
		res={'message':msg, 'probability': prob}
		return render_template('result.html', data=res, msg=msg1)
	return render_template('index.html')

@app.route('/headline')
def headline():
	news_data=hd.main()
	total=len(news_data)
	page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
	Pag_data=news_data[offset:offset+10]
	pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap4')
	return render_template('hotTopics.html',data=Pag_data, page=page, per_page=per_page,pagination=pagination)

@app.route('/contact',methods=['POST','GET'])
def contact():
	if request.method=='POST':
		name = request.form['name']
		email = request.form['email']
		msg = request.form['message']
		cur = mysql.connection.cursor()
		cur.execute("""insert into contact (name,email,message) values(%s,%s,%s)""",(name,email,msg))
		mysql.connection.commit()
		cur.close()
		return render_template('index.html')
	return render_template('index.html')





if __name__=='__main__':
	app.run(debug=True)
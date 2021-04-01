from flask import Flask, render_template, request, url_for
import prediction as pred

app=Flask(__name__, static_folder='static', template_folder='templates')
import headline as hd

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
	return render_template('hotTopics.html',data=news_data)


if __name__=='__main__':
	app.run(debug=True)
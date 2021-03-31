from flask import Flask, render_template, request, url_for
app=Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/headline')
def headline():
	return render_template('hotTopics.html')


if __name__=='__main__':
	app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

posts = [
	{
		'author': 'Corey Taylor',
		'title': 'slipknot',
		'content': 'music',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Joey',
		'title': 'whatever',
		'content': 'music',
		'date_posted': 'April 09, 2018'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html' , posts = posts)

@app.route('/about')
def about():
	return render_template('about.html' , title = about)

if __name__ == '__main__':
	app.run(debug=True)

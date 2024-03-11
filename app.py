from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def load_html():
	print('HTML page is loaded')
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
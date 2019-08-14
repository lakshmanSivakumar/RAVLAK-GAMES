from flask import *
from functools import wraps

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/rps')
def rps():
	return render_template('rps.html')

@app.route('/floppy')
def floppy():
	return render_template('Flappy Bird.html')

if __name__=='__main__':
    app.run(host = '127.0.0.1', port=3000, debug = True)




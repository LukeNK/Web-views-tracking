from flask import Flask, request
import random
import string
app = Flask('app')

@app.route('/')
def root():
	f = open('home.html', 'r')
	return(f.read())

@app.route('/file/<f_name>')
def file(f_name):
	f = open('file/{}.html'.format(f_name), 'r')
	return(f.read())

@app.route('/h')
def host():
	num = 0
	length = 10 #overkill lol
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for i in range(length))
	f = open('file/' + result_str + '.txt', 'w+')
	f.write(str(num))
	f.close()
	return('''
	<p>Paste the following code to your website that need to track views:<br>
		<code>
		&lt;link href="https://web-views-tracking.lukenk.repl.co/count/{link}" rel="stylesheet"&gt;
		</code><br>
	To view your views: go to the following page:<br>
		<a href="https://web-views-tracking.lukenk.repl.co/views/{link}">https://web-views-tracking.lukenk.repl.co/views/{link}</a>

	</p>
	'''.format(link = result_str))

@app.route('/count/<f_name>')
def count(f_name):
	a = open('file/{}.txt'.format(f_name), 'r')
	c_v = int(a.read())
	v = c_v + 1
	a.close()
	f = open('file/{}.txt'.format(f_name), 'w')
	f.write(str(v))
	f.close()
	return('')

@app.route('/views/<f_name>')
def views(f_name):
	f = open('file/' + f_name + '.txt', 'r')
	return(f.read())

@app.route('/cli',methods = ['POST'])
def cli():
	respond = request.form.get('respond')
	code = request.form.get('code')
	num = 0
	length = 10 #overkill lol
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for i in range(length))
	f = open('file/' + result_str + '.txt', 'w+')
	f.write(str(num))
	f.close()
	if respond == "link":
		return('https://Web-views-tracking.lukenk.repl.co/count/' + result_str)
	elif respond == 'code':
		return(result_str)
	elif respond == 'html':
		return('<link href="https://web-views-tracking.lukenk.repl.co/count/{link}" rel="stylesheet">'.format(link=result_str))
	elif respond == 'count':
		return('https://web-views-tracking.lukenk.repl.co/views/{link}'.format(link=result_str))
	elif respond == 'check' and code != '':
		f = open('file/' + code + '.txt', 'r')
		return(f.read())
	return('Wrong input!')

app.run(host='0.0.0.0', port=8080)
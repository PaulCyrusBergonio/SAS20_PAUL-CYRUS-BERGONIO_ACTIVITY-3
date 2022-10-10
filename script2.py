from flask import *
app = Flask(_name_)

@app.route('/')
def message():
	return render_template('message.html')
if _name_ == '_main_':
	app.run(debug = True)
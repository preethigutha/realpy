from flask import Flask
app = Flask(__name__)
@app.route("/integer/<int:value>")
def int_type(value):
	print(value +1)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value +1)
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"

if __name__=="__main__":
	app.run()
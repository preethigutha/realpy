from flask import Flask
app = Flask(__name__)
@app.route("/name/<name>")
def index(name):
	if name.lower()=="preethi":
		return "HELLO,{}".format(name)
	else:
		return "NOT FOUND",404
if __name__=="__main__":
	app.run()
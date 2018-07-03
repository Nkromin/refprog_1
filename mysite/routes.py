from flask import Flask, render_template
import sys
import subprocess
from Indi import callout
from ModiStream import start_stream
from RahulStream import restart_stream



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
if __name__== "__main__":
	app.run(debug=True)
	response = callout(10)
	response = restart_stream(11)
	response = start_stream(12)




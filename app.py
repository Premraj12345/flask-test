from flask import Flask

app = Flask(__name__)
link = "Inkem.jpg"
@app.route("/")
def html():
	return f"""
	<img src="{link}"></img>
	
	"""

app.run()

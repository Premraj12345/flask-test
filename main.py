from flask import Flask

import base64

app = Flask(__name__)


def cvt_2_base64(file_name):
    with open(file_name , "rb") as image_file :
        data = base64.b64encode(image_file.read())
    return data.decode('utf-8')
    
   

t = "data:image/jpg;base64,"
b = cvt_2_base64("Inkem.jpg")

link = t+ b

@app.route("/")
def html():
	return f"""
	<img src="{link}"></img>
	
	"""

app.run()
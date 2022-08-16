from flask import Flask
from main import 
app = Flask(__name__)

@app.route('/')
def main():
    img = 'Inkem.jpg'
    return f'''
    <img src="/{img}"></img>
    '''
@app.route('/proxylist')
def proxylist2():
    return 
if __name__ == '__main__':
    app.run()

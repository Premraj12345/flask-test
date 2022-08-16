from flask import Flask
from main import valid_proxies2
app = Flask(__name__)

@app.route('/')
def main():
    img = 'https://raw.githubusercontent.com/Premraj12345/flask-test/main/Inkem.jpg'
    return f'''
    <img src="{img}"></img>
    '''
@app.route('/proxylist')
def proxylist2():
    return f'{valid_proxies2}'

if __name__ == '__main__':
    app.run()

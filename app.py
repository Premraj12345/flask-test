from flask import Flask
from main import valid_proxies2

app = Flask(__name__)

@app.route('/')
def main():
    return '<h2> Hello World <h2>'
@app.route('/proxylist')
def proxylist2():
    return f'{valid_proxies2}'

if __name__ == '__main__':
    app.run()

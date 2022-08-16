from flask import Flask


app = Flask(__name__)

valid_proxies = []
valid_proxies2 = []

@app.route('/')
def main():
    return '<h2> Hello World <h2>'

@app.route('/setproxylist/<ipport>')
def setproxylist():
    valid_proxies.append(ipport)
    return '<h1>Success<h1>'

@app.route('/proxylist')
def proxylist():
    return f'{valid_proxies2}'

@app.route('/clearlist')
def clearlist():
    return '<h1>Succesfully Cleared<h1>'

@app.route('/proxyaddto2')
def proxyaddto2():
    valid_proxies2 = valid_proxies

if __name__ == '__main__':
    app.run()

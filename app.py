from flask import Flask


app = Flask(__name__)

valid_proxies = []

@app.route('/')
def main():
    return '<h2> Hello World <h2>'

@app.route('/setproxylist/<ipport>')
def setproxylist(ipport):
    valid_proxies.append(ipport)
    return '<h1>Success<h1>'

@app.route('/proxylist')
def proxylist():
    return f'{valid_proxies}'

@app.route('/clearlist')
def clearlist():
    valid_proxies.clear()
    return '<h1>Succesfully Cleared valid_proxies List<h1>'

if __name__ == '__main__':
    app.run()

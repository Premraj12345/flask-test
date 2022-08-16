from flask import Flask


app = Flask(__name__)

valid_proxies = []
valid_proxies2 = []

@app.route('/')
def main():
    return '<h2> Hello World <h2>'

@app.route('/setproxylist/<ipport>')
def setproxylist(ipport):
    valid_proxies.append(ipport)
    return '<h1>Success<h1>'

@app.route('/proxylist')
def proxylist():
    return f'{valid_proxies2}'

@app.route('/clearlist')
def clearlist():
    valid_proxies.clear()
    return '<h1>Succesfully Cleared valid_proxies List<h1>'

@app.route('/clearlist2')
def clearlist2():
    valid_proxies2.clear()
    return '<h1> Successfully Cleared valid_proxies2 List<h1>'

@app.route('/proxyaddto2')
def proxyaddto2():
    valid_proxies2.append(valid_proxies)
    return '<h1>Succesfully added to valid_proxies2 <h1>'
if __name__ == '__main__':
    app.run()

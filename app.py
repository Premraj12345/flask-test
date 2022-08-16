from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    img = 'Inkem.jpg'
    return f'''
    <img src="/{img}"></img>
    '''
if __name__ == '__main__':
    app.run()

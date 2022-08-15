from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    img = 'Inkem.jpg'
    return f'''
    <img src="{img}"></img>
    '''
app.run()

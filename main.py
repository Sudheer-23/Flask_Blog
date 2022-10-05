from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def greet(name):
    return 'Hello {}'.format(name)

if(__name__ == '__main__'):
    app.run(debug=True)
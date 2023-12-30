# Inside app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forgiven')
def forgiven():
    return render_template('forgiven.html')

@app.route('/not_forgiven')
def not_forgiven():
    return render_template('not_forgiven.html')

if __name__ == '__main__':
    app.run(debug=True)

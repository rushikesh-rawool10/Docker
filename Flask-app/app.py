from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Dosto!'

@app.route('/about')
def about():
    return 'This is a simple Flask app.'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/template_example')
def template_example():
    return render_template('index.html', message='This is a template example.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='首页', theme='dark')

@app.route('/about')
def about():
    return render_template('about.html', title='关于我们', theme='dark')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='联系我们', theme='dark')

if __name__ == '__main__':
    app.run(debug=True)

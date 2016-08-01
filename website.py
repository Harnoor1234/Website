import jinja2
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/experiences/')
def experiences():
    return render_template('experiences.html')
@app.route('/project/')
def projects():
    return render_template('projects.html')
if __name__ == '__main__':
    app.run(debug=True)

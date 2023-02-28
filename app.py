"""Flask application with embedded chatbot and analytics"""
from flask_bootstrap import Bootstrap
from flask import Flask, render_template


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analytics')
def user(name):
    return render_template('analytics.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

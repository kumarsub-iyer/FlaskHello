from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return {"message": "Hello from Kumar to try a Flask app in Vercel!"}

@app.route('/about')
def about():
    return {"status": "success", "page": "about"}

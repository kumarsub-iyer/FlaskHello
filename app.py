from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from Kumar to try a Flask app in Vercel!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}, POST request received"
    return render_template('name.html')


@app.route('/about')
def about():
    return {"status": "success", "page": "about"}

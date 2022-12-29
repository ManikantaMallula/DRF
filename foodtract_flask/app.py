from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add')
def add():
    return render_template('day.html')

@app.route('/food')
def food():
    return render_template('add_food.html')

if __name__ == '__main__':
    app.run(debug=True)
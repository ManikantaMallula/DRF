from flask import Flask, request, render_template, url_for, flash, redirect
import sqlite3
import os
from flask_session import Session
from forms import AddItemForm, AddDateForm


app = Flask('__name__')
app.config['SECRET_KEY'] = 'flask303'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, r'media\profile_pics')
Session(app)

print(app.root_path)

connection = sqlite3.connect('database.db')

connection.execute('create table IF NOT EXISTS  FoodItem (Fooditem text PRIMARY KEY,quantity text, calories text, fat text, carbohydrates text'
                   ', protein text, category text)')
connection.execute('create table IF NOT EXISTS AddDate (date text PRIMARY KEY)')
connection.execute('create table AddDetail (add_item text, FOREIGN KEY(add_item) REFERENCES FoodItem(Fooditem) ,'
                   'date_d text,  FOREIGN KEY(date_d) REFERENCES AddDate(date))')

# connection.execute('create table TotalEnergies (date text, total_pro text, total_carbo text, '
#                    'total_fat text, total_cal text)')
#
connection.close()

@app.route('/addfood', methods=['GET', 'POST'])
def FoodItemPage():
    form = AddItemForm()
    if request.method == "POST":
        Fooditem = request.form['Fooditem']
        quantity = request.form['quantity']
        calories = request.form['calories']
        fat = request.form['fat']
        carbohydrates = request.form['carbohydrates']
        protein = request.form['protein']
        category = request.form['category']
        with sqlite3.connect('database.db') as con:
            con.execute('insert into FoodItem (Fooditem, quantity, calories, fat, carbohydrates, protein, category) '
                        'values (?, ?, ?, ?, ?, ?, ?)', (Fooditem, quantity, calories, fat, carbohydrates, protein, category))

        return redirect('/addfood')
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute('select * from FoodItem')
    rows = cur.fetchall()
    return render_template('item_details.html', form=form, rows=rows)


@app.route('/', methods=['GET', 'POST'])
def Home():
    form = AddDateForm()
    if request.method=='POST':
        date = request.form['date']
        with sqlite3.connect('database.db') as con:
            con.execute('insert into AddDate(date) values(?)', (date,))

        return redirect('/')
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    connection.row_factory = sqlite3.Row
    cur.execute('select * from AddDate')
    rows = cur.fetchall()
    return render_template('home.html', form=form, rows=rows)

# app.route('/details/<int:id>/')
# def Details(id):
#     if request.method=='POST':
#         form = AddDetailForm(request.form)




if __name__ == '__main__':
    app.run(debug=True)
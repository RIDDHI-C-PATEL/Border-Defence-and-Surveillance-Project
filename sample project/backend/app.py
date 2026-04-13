from flask import Flask, render_template, request, jsonify, redirect
import sqlite3
import random

# Create Flask App First
app = Flask(__name__, template_folder='../templates')


def connect_db():
    return sqlite3.connect("database/border.db")


@app.route('/login', methods=['GET','POST'])
def login():

    if request.method=='POST':

        user=request.form['username']
        pwd=request.form['password']

        if user=='admin' and pwd=='admin':
            return redirect('/military')

    return render_template('login.html')


@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')


@app.route('/drone')
def drone():
    return render_template('drone.html')


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/cctv')
def cctv():
    return render_template('cctv.html')


@app.route('/satellite')
def satellite():
    return render_template('satellite.html')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/map")
def map():
    return render_template("map.html")


@app.route("/military")
def military():
    return render_template("military_dashboard.html")


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route("/add_alert", methods=['POST'])
def add_alert():

    data = request.json

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO alerts(type,location,confidence)
    VALUES(?,?,?)
    """,(data['type'],data['location'],data['confidence']))

    conn.commit()
    conn.close()

    return jsonify({"message":"Added"})


@app.route("/get_alerts")
def get_alerts():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alerts")
    data = cursor.fetchall()

    conn.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from mail import *
import psycopg2

app = Flask(__name__)

host="23.96.93.237"
dbname="postgres"
user="postgres"
password="123"

conn_string = "host={0} dbname={1} user={2} password={3}".format(host, dbname, user, password)
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

def get_data(email_user): 
    host="23.96.93.237"
    dbname="postgres"
    user="postgres"
    password="123"

    conn_string = "host={0} dbname={1} user={2} password={3}".format(host, dbname, user, password)
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO email_adress (email) VALUES ('{email_user}')")
    conn.commit()

@app.route('/home')
def welcome(): 
        return render_template("index.html")

@app.route('/form', methods=["GET", "POST"])
def form(): 
    if request.method == "POST":
        user_email=request.form["email"]
        get_data(user_email)
        sendmail(user_email)

        return render_template ("form.html")

'''@app.route('/api')
def api():
    cursor.execute("SELECT * FROM Carpet, Mirror WHERE Carpet.ID = Mirror.ID ORDER BY Carpet.ID")
    output = cursor.fetchall()
    return jsonify(output)

@app.route('/api_carpet')
def api_carpet(): 
    cursor.execute("SELECT * FROM Carpet")
    output = cursor.fetchall()
    return jsonify(output)

@app.route('/api_mirror')
def api_mirror(): 
    cursor.execute("SELECT * FROM Mirror")
    output = cursor.fetchall()
    return jsonify(output)

@app.route('/api_carpet_price')
def ranking_price_carpet(): 
    #http://http://localhost:4050/api_carpet_price?PRIX=200

    carpet_price = request.args.get("PRIX")

    cursor.execute("SELECT * FROM Carpet WHERE PRIX <= ('%s')" %(carpet_price))
    #print(result)
    output = cursor.fetchall()
    #print(output)
    return jsonify(output)

@app.route('/api_mirror_price')
def ranking_price_mirror(): 
    #http://http://localhost:4050/api_mirror_price?PRIX=200

    mirror_price = request.args.get("PRIX")

    cursor.execute("SELECT * FROM Mirror WHERE PRIX <= ('%s')" %(mirror_price))
    output = cursor.fetchall()
    return jsonify(output)'''

#if __name__ == "__main__": 
    #app.run(host= "0.0.0.0", port=3050, debug = True)
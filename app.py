from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

fields_of_study = ["Computer Science", "Mathematics", "Physics", "Chemistry"]
fields_of_interest = ["AI", "ML", "Data Science", "IoT"]

def create_table():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS events
                 (event_name text, event_description text, fields_of_study text, fields_of_interest text)""")
    conn.commit()
    conn.close()

@app.route("/")
def form():
    return render_template("form.html", fields_of_study=fields_of_study, fields_of_interest=fields_of_interest)

@app.route("/submit", methods=["POST"])
def submit():
    event_name = request.form["event_name"]
    event_description = request.form["event_description"]
    fields_of_study = ','.join(request.form.getlist("fields_of_study"))
    fields_of_interest = ','.join(request.form.getlist("fields_of_interest"))

    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("INSERT INTO events VALUES (?,?,?,?)", (event_name, event_description, fields_of_study, fields_of_interest))
    conn.commit()
    conn.close()

    return "Event Submitted"

def get_data():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT * FROM events")
    rows = c.fetchall()
    return rows

@app.route("/data")
def data():
    events_data = get_data()
    return jsonify({"events": events_data})

if __name__ == "__main__":
    create_table()
    app.run(debug=True)

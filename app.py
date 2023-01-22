from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

categories = '''Technical workshops
Technical competitions (such as coding, robotics, hacking, etc.)
Business case study competitions
Entrepreneurship events
Guest lectures and panel discussions
Cultural events (such as music, dance, and drama performances)
Sports events
Project exhibitions
Networking and recruitment events
Gaming and quizzes
Robotics competitions
Debate competitions
Quiz competitions
Business plan competitions
Innovation competitions
Debate competitions
Photography competitions
Online events (such as webinars, online coding competitions, etc.)
Virtual reality events
Augmented reality events
IoT workshops
AI workshops
Machine learning workshops
Blockchain workshops
Cybersecurity workshops
Digital marketing workshops
Social media marketing workshops
Design thinking workshops
Leadership workshops
Innovation workshops
Business model workshops
Networking events
Career fairs
Alumni meets
Hackathon
Coding competitions
Gaming competitions
Film festivals
Food festivals
Cultural events
Music competitions
Dance competitions
Theater performances
Poetry slam
Comedy nights
Art exhibitions
Science exhibitions
Environmental conservation events
Women empowerment events
Start-up exhibitions
Industry-academia interactions
International delegations
Professional development workshops
Student mentor interactions
Entrepreneurial mentoring sessions
Career guidance sessions
Industry visits
Leadership development programs
Technical training programs
Student exchange programs
Internship opportunities
Scholarship opportunities
Awards and recognition ceremonies
Closing ceremonies
Networking events
Job fairs
Social service events
Blood donation camps
Tree plantation drives
Yoga and meditation sessions
Adventure sports
Zumba sessions
Fitness competitions
Swimming competitions
Chess competitions
Carrom competitions
Table tennis competitions
Badminton competitions
Volleyball competitions
Football competitions
Cricket competitions
Basketball competitions
Tennis competitions
Athletics competitions
Book fairs
Comic con
Cosplay competitions
Treasure hunt
Escape room
Scavenger hunt
Debate competitions
Stand-up comedy
Magic shows
Illusion shows
Celebrity performances
Fireworks displays
Laser shows
Light shows
Sound and light shows
DJ nights
EDM nights
Cultural nights
Folk nights
Classical music nights'''

interests = '''Music
Festival
Entertainment
Visual Arts
Exhibition
Creative
Technology
Competition
Innovative
Food
Culinary
Sports
Outdoor
Career
Fair
Networking
Performing Arts
Drama
Theater
Literary Arts
Poetry
Comedy
Humor
Dance
Environmental
Entrepreneurship
Gaming
Health & Wellness
Leadership
Professional Development
Science & Technology
Social Justice
Volunteerism
Photography
Fashion
Business
Design
Film & Media
International
Political
Women's Issues
Yoga
Travel'''


fields_of_study = categories.split("\n")
fields_of_interest = interests.split("\n")

# def create_table():
#     conn = sqlite3.connect('test.db')
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS events
#                  (event_name text, event_description text, fields_of_study text, fields_of_interest text)""")
#     conn.commit()
#     conn.close()

# @app.route("/")
# def form():
#     return render_template("form.html", fields_of_study=fields_of_study, fields_of_interest=fields_of_interest)

# @app.route("/submit", methods=["POST"])
# def submit():
#     event_name = request.form["event_name"]
#     event_description = request.form["event_description"]
#     fields_of_study = ','.join(request.form.getlist("fields_of_study"))
#     fields_of_interest = ','.join(request.form.getlist("fields_of_interest"))

#     conn = sqlite3.connect('test.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO events VALUES (?,?,?,?)", (event_name, event_description, fields_of_study, fields_of_interest))
#     conn.commit()
#     conn.close()

#     return "Event Submitted"

# def get_data():
#     conn = sqlite3.connect('test.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM events")
#     rows = c.fetchall()
#     return rows

# @app.route("/data")
# def data():
#     events_data = get_data()
#     return jsonify({"events": events_data})

# if __name__ == "__main__":
#     create_table()
#     app.run(debug=True)

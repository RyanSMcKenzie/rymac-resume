from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def resume():
    res = """
RYAN MCKENZIE
=====================

Education
=====================
B.S. Computer Science - Oregon State University
B.S. Biology - Purdue University

Experience
=====================
Software Engineering Intern - Bluestaq LLC
Summer 2021
- I will be working on Java/Maven backend systems

Undergraduate Learning Assistant - Oregon State University
March 2020 - Present
- Grade assignments, leave feedback regarding code optimization
- Hold office hours to clarify assignment details and code concepts

Projects
=====================
Dungeoneer's Flask - D&D Character Sheet Flask App
Link: http://github.com/RyanSMcKenzie/DungeonFlask
- Login, logout, and character browsing with Flask/Jinja
- Save and load characters and character data with Google Firestore
- Automated testing, integration, and branch protection with TravisCI
- Containerized with Docker and continuously deployed on Google Cloud Run

A Shape's Journey - Terminal Java/Maven RPG
Link: http://github.com/RyanSMcKenzie/A Shapes Journey
- Object-oriented Java terminal RPG
- Uses Maven for build and dependency management
- JSON saving and loading of player character data
- ANSI terminal coloring for item rarity, randomly generated loot
- Experience and level-up dynamics

Self.get(Well) - Flutter/Dart mental health app
Link: http://github.com/RyanSMcKenzie/Self_Get_Well
- Flutter mobile app for mental wellness self-tracking
- Daily check-in stores data in SQLite database, displays graph of past self-reports
- Help page with hotline buttons, which make calls from your phone via the app
- Resources page with active web link buttons

Skills
=====================
Languages - Java, Python, JavaScript, HTML, CSS, Swift, Dart, C, SQL
Frameworks - Node.js, Express.js, Flask, Firestore, Flutter, Maven
Other - Agile, Git, TravisCI, Docker\n\n"""
    return res

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    # Run app
    app.run(host="0.0.0.0", port=port, debug=True)
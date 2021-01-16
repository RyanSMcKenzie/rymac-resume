from flask import Flask
import os

# Deploy curl https://rymac-resume.herokuapp.com/
app = Flask(__name__)

@app.route('/')
def resume():
    res = """

Here's an abridged version of my resume! For more instructions:

'curl https://rymac-resume.herokuapp.com/help'

RYAN MCKENZIE
rmckenzieswe@gmail.com
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
Link: http://github.com/RyanSMcKenzie/A_Shapes_Journey
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

@app.route('/help')
def assist():
    ret = """
    Interested to know more about me? 
    Visit '/cover' for a generalized cover letter

    More about my education?
    Visit '/education' for more on my education

    More about my experience?
    Visit '/experience' for more on my experience
    
    """
    return ret

@app.route('/cover')
def cover():
    ret = """
To Whom It May Concern,

My name's Ryan, and I'm interested in becoming a software engineer. My first
degree was in biology, but I pivoted to software engineering after graduating,
and began studying Computer Science at Oregon State University. I love to learn
and I love the puzzle-like problem-solving aspects of software engineering. As
an engineer, I am partial to backend engineering. I love to mess with the
'guts' of software, and work with the internal logic that makes it all come
together. Above all, I'm most interested in working somewhere where I can learn
and grow as much as possible. The stack is not so important to me as the
ability to improve my skills, work with smart people, and grow as a person and
as an engineer. 

Whoever reads this, I hope we get the chance to talk more and discuss how I
might be able to contribute to your company and learn some awesome things.

For contact details, please see the resume page on the '/' route. Thanks!


Ryan
    """
    return ret

@app.route('/education')
def edu():
    ret = """
Hi there! Here's some extra info about my educational background:

Bachelor's Degree - Biology - Purdue University
Dates: August 2015 - May 2019
GPA: 3.8
Details: At Purdue, I studied biology. My primary focus was on molecular and
cell biology. This includes applied molecular biology, endocrinoloy, etc.

Bachelor's Degree - Computer Science - Oregon State University
Dates: January 2020 - August 2021
GPA: 4.0
Details: After Purdue, I joined the OSU Post-Bacc CS program. The core program
primarily focuses on software engineering and general CS fundamentals, and I am
taking network and cloud development electives.

    """
    return ret

@app.route('/experience')
def exp():
    ret = """
Software Engineering Intern - Bluestaq LLC
Dates: June 1 - ???, 2021
Details: This is my summer internship for the year 2021. I will be
working with Java/Maven enterprise systems in the aerospace domain. 
Official details are currently uncertain.

Undergraduate Learning Assistant - Oregon State University
Dates: March 2020 - Present
Details: As a ULA at OSU, I help teach an introductory programming course. As a
general rule, I grade assignments weekly and give feedback on the code, whether
it's an error correction or an idea about how the code could be optimized or
modified to fit convention. I also have office hours each week where I help
students to get through the assignments or just answer questions about
programming in general.

Teaching Assistant - Purdue University
Dates: January 2019 - August 2019
Details: As a TA at Purdue, I taught multiple live-coding labs in Python
object-oriented programming, as well as graded homework and held office hours.
The labs often included a lengthy problem meant to be solved in about two hours
which I supervised and helped with. Office hours involved me helping with long
projects students were assigned over multiple weeks, which often were small
games with GUIs. During this time, I was also asked to help design assignments
and exams for a new introductory data science class which made use of scipy, 
pandas, numpy, and the like.

    """
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    # Run app
    app.run(host="0.0.0.0", port=port, debug=True)
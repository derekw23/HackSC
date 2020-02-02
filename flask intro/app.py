from flask import Flask, render_template, url_for, request
import dataFrameTest as dft
from dataFrameTest import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

feels = []
emotions = []
sleeps = []
assignments = []
googles = []

@app.route('/', methods=["GET"])
def index():
    return render_template('HackSCHomePage.html')

@app.route('/inputs', methods=["GET"])
def inputs():
    return render_template('inputs.html')

#@app.route('/calendar', methods=["GET"])
#def calendar():
#    return render_template('calendar.html')

@app.route('/notinputs', methods=["GET"])
def notinputs():
    return render_template('notinputs.html')

@app.route('/HackSCHomePage', methods=["GET"])
def HackSCHomePage():
    return render_template('HackSCHomePage.html')

@app.route('/addfeel', methods = ['POST', 'GET'])
def addfeel():
    feel = request.form["feel"]
    dft.setHappiness(feel)
    feels.append(feel)
    print(feels)
    return render_template('inputs.html', feel=feel)

@app.route('/addemotion', methods = ['POST', 'GET'])
def addemotion():
    emotion = request.form["emotion"]
    dft.setEmotions(emotion)
    emotions.append(emotion)
    print(emotions)
    return render_template('inputs.html', emotion=emotion)

@app.route('/addsleep', methods = ['POST', 'GET'])
def addsleep():
    sleep = []
    weekday = request.form["weekday"]
    sleep.append(weekday)
    weekend = request.form["weekend"]
    sleep.append(weekend)
    dft.setNightTime(weekday, weekend)
    sleeps.append(sleep)
    print(sleeps)
    return render_template('inputs.html', weekday=weekday, weekend=weekend)

@app.route('/addassign', methods = ['POST', 'GET'])
def addassign():
    assigns = []
    name = request.form["aname"]
    dft.addAssignmentName(name)
    assigns.append(name)
    workload = request.form["aworkload"]
    dft.addWorkLoad(workload)
    assigns.append(workload)
    date = request.form["adate"]
    dft.addDate(date)
    assigns.append(date)
    assignments.append(assigns)
    print(assignments)
    return render_template('inputs.html', a1=a1, a2=a2, a3=a3, a4=a4)

@app.route('/addgoogle', methods = ['POST', 'GET'])
def addgoogle():
    google = request.form["google"]
    googles.append(google)
    print(googles)
    return render_template('inputs.html', google=google)

@app.route('/nextpage', methods = ['POST', 'GET'])
def nextpage():
    ev = dft.html_table()
    return render_template('calendar.html', ev=ev)


if __name__ == '__main__':
    app.run(debug=True)
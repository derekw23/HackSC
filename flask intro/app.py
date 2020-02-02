from flask import Flask, render_template, url_for, request
from dataFrameTest import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
#help = []
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

@app.route('/calendar', methods=["GET"])
def calendar():
    return render_template('calendar.html')

@app.route('/notinputs', methods=["GET"])
def notinputs():
    return render_template('notinputs.html')

@app.route('/HackSCHomePage', methods=["GET"])
def HackSCHomePage():
    return render_template('HackSCHomePage.html')

@app.route('/addfeel', methods = ['POST', 'GET'])
def addfeel():
    feel = request.form["feel"]
    feels.append(feel)
    print(feels)
    return render_template('inputs.html', feel=feel)

@app.route('/addemotion', methods = ['POST', 'GET'])
def addemotion():
    emotion = request.form["emotion"]
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
    sleeps.append(sleep)
    print(sleeps)
    return render_template('inputs.html', weekday=weekday, weekend=weekend)

@app.route('/addassign', methods = ['POST', 'GET'])
def addassign():
    assigns = []
    name = request.form["aname"]
    assigns.append(name)
    priority = request.form["apriority"]
    assigns.append(priority)
    workload = request.form["aworkload"]
    assigns.append(workload)
    date = request.form["adate"]
    assigns.append(date)
    assignments.append(assigns)
    print(assignments)
    return render_template('inputs.html', a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7)

@app.route('/addgoogle', methods = ['POST', 'GET'])
def addgoogle():
    google = request.form["google"]
    googles.append(google)
    print(googles)
    return render_template('inputs.html', google=google)


if __name__ == '__main__':
    app.run(debug=True)
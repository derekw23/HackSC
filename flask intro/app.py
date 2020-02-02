from flask import Flask, render_template, url_for, request
from dataFrameTest import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
help = []

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
    help.append(feel)
    print(help)
    return render_template('inputs.html', feel=feel)

@app.route('/addemotion', methods = ['POST', 'GET'])
def addemotion():
    emotion = request.form["emotion"]
    help.append(emotion)
    print(help)
    return render_template('inputs.html', emotion=emotion)

@app.route('/addsleep', methods = ['POST', 'GET'])
def addsleep():
    sleep = []
    weekday = request.form["weekday"]
    sleep.append(weekday)
    weekend = request.form["weekend"]
    sleep.append(weekend)
    help.append(sleep)
    print(help)
    return render_template('inputs.html', weekday=weekday, weekend=weekend)

@app.route('/addassign', methods = ['POST', 'GET'])
def addassign():
    assigns = []
    a1 = request.form["assignment1"]
    assigns.append(a1)
    a2 = request.form["assignment2"]
    assigns.append(a2)
    a3 = request.form["assignment3"]
    assigns.append(a3)
    a4 = request.form["assignment4"]
    assigns.append(a4)
    a5 = request.form["assignment5"]
    assigns.append(a5)
    a6 = request.form["assignment6"]
    assigns.append(a6)
    a7 = request.form["assignment7"]
    assigns.append(a7)
    help.append(assigns)
    print(help)
    return render_template('inputs.html', a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7)

@app.route('/addgoogle', methods = ['POST', 'GET'])
def addgoogle():
    google = request.form["google"]
    help.append(google)
    print(help)
    return render_template('inputs.html', google=google)


if __name__ == '__main__':
    app.run(debug=True)
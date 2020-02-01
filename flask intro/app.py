from flask import Flask, render_template, url_for
from dataFrameTest import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

@app.route('/', methods=["GET"])
def index():
    return render_template('HackSCHomePage.html')

@app.route('/inputs', methods=["GET"])
def inputs():
    return render_template('inputs.html')

@app.route('/calendar', methods=["GET"])
def calendar():
    return render_template('calendar.html')

@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
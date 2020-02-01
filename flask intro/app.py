from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('HackSCHomePage.html')

@app.route('/inputs', methods=["GET"])
def inputs():
    return render_template('inputs.html')

@app.route('/calendar', methods=["GET"])
def calendar():
    return render_template('calendar.html')


if __name__ == '__main__':
    app.run(debug=True)
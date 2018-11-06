from flask import Flask
from emailAuto import emailAuto
app = Flask(__name__)

@app.route('/')
def index():
    return "It's Opaque!!!"

@app.route('/email')
def emailauto():
    test1 = emailAuto()
    test1.test()

if __name__ == '__main__':
    app.run()

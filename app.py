from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "testing API\nHello world!!"

app.run()


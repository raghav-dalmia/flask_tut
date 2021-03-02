import os
from flask import Flask

# Initialize application
app = Flask(__name__, static_folder=None)

@app.route('/')
def hello():
    return "testing API\nHello world!!"

app.run()


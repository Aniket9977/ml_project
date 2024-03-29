from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route('/' , methods = ['GET' , "POST"])

def index():
    logging.info('we are testing the logging modeulee')
    return 'CI CD pipline has been established'


def index():
    return 'Starting Machine learning project'


if __name__ =="__main__":
    app.run(debug = True)
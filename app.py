from flask import Flask
from housing.logger import logging
from housing.exception import housingException
import sys

app = Flask(__name__)

@app.route('/' , methods = ['GET' , "POST"])

def index():
    try:
        raise Exception('we are testing custom exception')
    
    except Exception as e:
        housing = housingException(e,sys)
        logging.info(housing.error_message)
        logging.info('we are testing the logging modeulee')
    return 'CI CD pipline has been established'


if __name__ =="__main__":
    app.run(debug = True)
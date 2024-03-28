from setuptools import setup
from typing import List


PROJECT_NAME = 'housing_predictor'
VERSION = "0.0.1"
AUTHOR = "Aniket"
DESCRIPTION = "This is the first ML project"
PACKAGE = ['housing']
REQ_FILE = 'req.txt'

def get_req_list()-> List[str]:
    """
    Description : this add all the req that need to be installed 
    """
    with open (REQ_FILE) as file:
        return file.readlines()

setup(
    name =PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGE,
    install_req = get_req_list()
    
)

if __name__ =='__main__':
    print(get_req_list())
#creates package app to be used and will host the application
from flask import Flask
#sets Flask class to __name__ which will set it to the module it is used in.
app = Flask(__name__)

from app import routes
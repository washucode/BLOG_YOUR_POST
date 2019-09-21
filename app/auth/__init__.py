# create blueprint
from flask import Blueprint
auth = Blueprint('auth', __name__)
from .view import *


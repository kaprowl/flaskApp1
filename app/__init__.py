from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '9aa1d6f8b2d4cefbe63cd1f1aaa694479aa4e7983a31da8d'

from app import views  # noqa

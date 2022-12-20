from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '7de9a5cfeb89d65d9c940fffdbf852e82d981e3e7e3acd17'
 
from app import views  # noqa
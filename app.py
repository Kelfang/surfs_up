# Import Flask.
from flask import Flask

# Create a new flask app instance.
app = Flask(__name__)

# Create first route. After the @ sign - put the name of the new flask app instance.

@app.route('/')
def hello_world():
    return 'Hello world'
    

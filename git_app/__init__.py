from flask import Flask 
app = Flask(__name__) 
 
app.secret_key = "some super secret key"

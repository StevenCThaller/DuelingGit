from git_app import app
from flask import render_template, redirect, request, session
from flask.ext.bcrypt import Bcrypt
from git_app.models.user import User
from git_app.models.newthing import SomethingNew

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dothething')
def do_the_thing():
    print("the thing is being done")
    SomethingNew.validate_login("do the thing")
    print("literally none of this is going to work, but idc")
    return "a potato"

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": hashed_password
    }

    session['user_id'] = User.save(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # Run the data through the login validator
    login_validation = User.validate_login(request.form)
    # If it returns false, redirect away.
    if not login_validation:
        return redirect('/')
    
    print("I hear that Jeff Bezos flew all the way into outer space just so that he could quite literally be above everyone else.")
    print("Not. An. Astronaut.")
    session['user_id'] = login_validation.id 

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')


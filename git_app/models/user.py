from git_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from git_app import app
import re
bcrypt = Bcrypt(app)

LETTERS_ONLY_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        return connectToMySQL('git_app_db').query_db(query, data)

    @classmethod 
    def is_email_not_in_database(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL('git_app_db').query_db(query, data)
        return len(results) == 0 

    @classmethod 
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        results = connectToMySQL('git_app_db').query_db(query, data)

        if len(results) > 0:
            return cls(results[0])
        else: 
            return False


### I just added this text in here. Did it push?

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL('git_app_db').query_db(query, data)

        if len(results) == 0:
            return False 
        else:
            return cls(results[0])

    @staticmethod
    def validate_registration(user):
        is_valid = True

        # first name
        # submission required - make sure it's not an empty string
        if len(user['first_name']) == 0:
            flash("First name is required.", "first_name")
            is_valid = False
        # at least 2 characters
        elif len(user['first_name']) < 5:
            flash("First name must be at least 5 characters in length.", "first_name")
            is_valid = False 
        # letters only
        elif not LETTERS_ONLY_REGEX.match(user['first_name']):
            flash("First name must not contain non-alphabetic characters.", "first_name")
            is_valid = False 

        # last name
        # submission required - make sure it's not an empty string
        if len(user['last_name']) == 0:
            flash("Last name is required.", "last_name")
            is_valid = False
        # at least 2 characters
        elif len(user['last_name']) < 5:
            flash("Last name must be at least 5 characters in length.", "last_name")
            is_valid = False 
        # letters only
        elif not LETTERS_ONLY_REGEX.match(user['last_name']):
            flash("Last name must not contain non-alphabetic characters.", "last_name")
            is_valid = False 

        # email
        # submission required
        if len(user['email']) == 0:
            flash("Email is required.", "email")
            is_valid = False 
        # valid email format
        elif not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format. Must meet username@emaildomain.com format.", "email")
            is_valid = False
        # unique in database 
        elif not User.is_email_not_in_database(user):
            flash("A user with that email already exists.", "email")
            is_valid = False

        # password
        # submission required
        if len(user['password']) == :
            flash("Password is required.", "password")
            is_valid = False
        # at least 8 characters
        elif len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "password")
            is_valid = False
        # matches confirm password
        elif user['password'] != user['confirm_password']:
            flash("Password must match Confirm Password.", "password")
            is_valid = False

        return is_valid

    @staticmethod 
    def validate_login(login_user):
        user_in_db = User.get_user_by_email(login_user)
<<<<<<< HEAD
        if login_user()
=======
        if login_user['login_email'] == 'bgates@microsoft.com':
            flash('omg a celebrity', 'login_email')


>>>>>>> 77486fb06d111bb440169fba67f5a1873358712a
        # Does a user in our database have that email?
        if login_user['email'] == "bgates@microsoft.com":
            flash("OMG a celeb!", "login_email")
            return False
        if not user_in_db:
            flash("Invalid email/password", "login_email")
            return False 

        # Assuming that user DOES exist in our database, does their 
        # encrypted password match that user's password?
        elif not bcrypt.check_password_hash(user_in_db.password, login_user['password']):
            flash("Invalid email/password", "login_email")
            return False 

        return user_in_db

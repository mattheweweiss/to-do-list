from flask import Blueprint, render_template, session


to_do_list = Blueprint("to_do_list", __name__, template_folder='templates')




# Default page route
@to_do_list.route('/')
def homepage():
    # Goes to the to-do list if user is logged in, homepage otherwise
    if session.get("user_id", None):
        return render_template('toDoList.html')
    else:
        return render_template('homepage.html')




# Route for login page
@to_do_list.route('/login', methods=['GET'])
def login():
    return render_template('login.html')




# Route for create account page
@to_do_list.route('/create_account', methods=['GET'])
def create_account():
    return render_template('createAccount.html')
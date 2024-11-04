from services.data_service import get_connection, open_cursor, close_cursor, close_connection

from flask import Blueprint, render_template


to_do_list = Blueprint("to_do_list", __name__, template_folder='templates')


# Default page route
@to_do_list.route('/')
def homepage():
    return render_template('homepage.html')



# Route for create account page
@to_do_list.route('/create_account', methods=['GET'])
def create_account():
    return render_template('create_account.html')
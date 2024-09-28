from services.data_service import get_connection, open_cursor, close_cursor, close_connection

from flask import Blueprint, render_template


auth = Blueprint("auth", __name__, template_folder='template')


# Route for login page
@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')
from services.data_service import get_connection, open_cursor, close_cursor, close_connection


from flask import Blueprint, request, render_template, redirect, url_for


auth = Blueprint("auth", __name__, template_folder='template')


# Route for login page
@auth.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        return redirect(url_for("to_do_list.homepage"))

    return render_template('login.html')
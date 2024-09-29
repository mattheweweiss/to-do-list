from services.auth_service import create_account


from flask import Blueprint, request, render_template, redirect, url_for


auth = Blueprint("auth", __name__, template_folder='template')


# Route for login page
@auth.route('/login', methods=["GET", "POST"])
def login_page():

    if request.method == "POST":
        return redirect(url_for("to_do_list.homepage"))

    return render_template('login.html')


# Route for create account page
@auth.route('/create_account', methods=["GET", "POST"])
def create_account_page():

    if request.method == "POST":

        # Getting fields from form
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        
        # Confirming password and confirm password fields match
        passwords = request.form.getlist("password")

        print(passwords[0])
        print(passwords[1])

        return redirect(url_for("to_do_list.homepage"))

    return render_template('create_account.html')
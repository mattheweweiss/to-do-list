from flask import Blueprint, request, render_template, redirect, url_for, jsonify
import os
import requests


auth = Blueprint("auth", __name__, template_folder='templates')




# Route for login page
@auth.route('/login', methods=["POST"])
def login():

    try:

        # Raises exception if a field isn't found
        if not request.form.get("email") or not request.form.get("password"):
            raise Exception("Missing field(s)")
        
        email = request.form.get("email")
        password = request.form.get("password")


        user_body = {
            "email": email,
            "password": password
        }

        
        # Login endpoint in application password manager
        login_endpoint = os.environ.get("LOGIN_ENDPOINT")


        # Sends request to endpoint in application password manager
        # Endpoint retrieves user from database and decrypts password hash to match to user input
        result = requests.get(login_endpoint, json = user_body)
        
        # Converts byte response to string
        result = result.content.decode()


        # If result is true, user is authenticated
        if result == "true":
            return redirect(url_for("to_do_list.homepage"))
        else:
            return render_template('login.html')

    except Exception as e:
        print(e)
        return render_template('login.html')

    



# Route for create account page
@auth.route('/create_account', methods=["POST"])
def create_account():

    try:

        # Raises exception if a field isn't found
        if not request.form.get("first-name") or not request.form.get("last-name") or not request.form.get("email") or not request.form.get("password"):
            raise Exception("Missing field(s)")


        # Getting fields from form
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        password = request.form.get("password")


        user_body = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }


        # Create account endpoint in application password manager
        create_account_endpoint = os.environ.get("CREATE_ACCOUNT_ENDPOINT")


        # Sends request to endpoint in application password manager
        # Endpoint creates user and user hash and user salt and stores in database
        requests.post(create_account_endpoint, json = user_body)
        
        return redirect(url_for("to_do_list.homepage"))
        
        
    except:
        return redirect(url_for("to_do_list.create_account"))
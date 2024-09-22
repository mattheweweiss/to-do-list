from flask import Blueprint, render_template


to_do_list = Blueprint("to_do_list", __name__, template_folder='templates')


@to_do_list.route('/')
def homepage():
    return render_template('homepage.html')
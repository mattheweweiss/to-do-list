from services.to_do_list_service import get_tasks, create_task, create_task_mapping

from flask import Blueprint, request, render_template, redirect, url_for, session
import datetime


to_do_list = Blueprint("to_do_list", __name__, template_folder='templates')




# Default page route
@to_do_list.route('/')
def homepage():

    # Goes to the to-do list if user is logged in, homepage otherwise
    if session.get("user_id", None):


        # Gets user tasks
        tasks_list = get_tasks()


        if tasks_list:

            # List of dictionary of tasks
            tasks = []


            # Formats tasks to send to template
            for task in tasks_list:
                

                # Creates dictionary of task information
                task_dict = {}
                task_dict["task"] = task[0]
                if task[1]:
                    task_dict["priority"] = task[1]
                task_dict["created_time_date"] = task[2].strftime('%m/%d/%Y')
                task_dict["created_time_time"] = task[2].strftime('%H:%M:%S')


                # Adds dictionary to list
                tasks.append(task_dict)


            # Renders to-do list template with tasks
            return render_template('toDoList.html', tasks = tasks)
        

        else:
            return render_template('toDoList.html')
    

    else:
        return render_template('homepage.html')




# Route for login page
@to_do_list.route('/login', methods=["GET"])
def login():
    return render_template('login.html')




# Route for create account page
@to_do_list.route('/create_account', methods=["GET"])
def create_account():
    return render_template('createAccount.html')




# Route to add task
@to_do_list.route('/add_task', methods=["POST"])
def add_task():

    # Retrieves body of request
    body = request.get_json()
    task = body["task"].replace("'", "''")
    priority = body["priority"]


    # Inserts task into table
    # Gets task_id
    task_id = create_task(task, priority)


    # Inserts task mapping into table
    if task_id > 0:
        create_task_mapping(task_id)


    return redirect(url_for('to_do_list.homepage'))
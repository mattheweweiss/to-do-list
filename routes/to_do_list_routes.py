from services.to_do_list_service import get_tasks, get_completed_tasks, create_task, create_task_mapping, update_task_complete

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
                task_dict["task_id"] = task[0]
                task_dict["task"] = task[1]
                if task[2]:
                    task_dict["priority"] = task[2]
                task_dict["created_time_date"] = task[3].strftime('%m/%d/%Y')
                task_dict["created_time_time"] = task[3].strftime('%H:%M:%S')


                # Adds dictionary to list
                tasks.append(task_dict)


            # Renders to-do list template with tasks
            return render_template('toDoList.html', tasks = tasks)
        

        else:
            return render_template('toDoList.html')
    

    else:
        return render_template('homepage.html')




# Route for completed tasks page
@to_do_list.route('/completed', methods=["GET"])
def completed():

    # Goes to the completed tasks if user is logged in, homepage otherwise
    if session.get("user_id", None):
        

        # Gets completed user tasks
        tasks_list = get_completed_tasks()


        if tasks_list:

            # List of dictionary of completed tasks
            tasks = []


            # Formats completed tasks to send to template
            for task in tasks_list:
                

                # Creates dictionary of completed task information
                task_dict = {}
                task_dict["task_id"] = task[0]
                task_dict["task"] = task[1]
                if task[2]:
                    task_dict["priority"] = task[2]
                task_dict["created_time_date"] = task[3].strftime("%m/%d/%Y")
                task_dict["created_time_time"] = task[3].strftime("%H:%M:%S")
                task_dict["completed_time_date"] = task[4].strftime("%m/%d/%Y")
                task_dict["completed_time_time"] = task[4].strftime("%H:%M:%S")


                # Adds dictionary to list
                tasks.append(task_dict)


            # Renders to-do list template with tasks
            return render_template('completed.html', tasks = tasks)


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
    priority = int(body["priority"])


    # Inserts task into table
    # Gets task_id
    task_id = create_task(task, priority)


    # Inserts task mapping into table
    if task_id > 0:
        create_task_mapping(task_id)


    return redirect(url_for('to_do_list.homepage'))




# Route to complete task
@to_do_list.route('/complete_task', methods=["POST"])
def complete_task():

    # Retrieves body of request
    body = request.get_json()
    task_id = int(body["taskId"])


    # Updates task to complete in table
    update_task_complete(task_id)


    return redirect(url_for('to_do_list.homepage'))
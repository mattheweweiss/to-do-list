from services.data_service import get_connection, open_cursor, close_cursor, close_connection

from flask import session
import os


# Getting database schema from .env
schema = os.environ.get("SCHEMA")




# Gets user tasks
def get_tasks():


    # Initializing result as empty list
    result = []


    # Retrieving user_id
    user_id = session.get("user_id", None)


    # Opens connection and cursor
    connection = get_connection()
    cursor = open_cursor(connection)


    try:

        # Searches for tasks of specified user
        select_tasks = f"""
            SELECT task_id
                ,task
                ,priority
                ,created_time
            FROM to_do_list.tasks AS t
            JOIN to_do_list.user_tasks AS ut
                ON t.id = ut.task_id
            WHERE ut.user_id = %s
                AND t.completed = 0
        """


        # Searches for tasks
        cursor.execute(select_tasks, (user_id, ))


        # Retrieves results
        result = cursor.fetchall()


        connection.commit()

    
    except Exception as e:
        print(e)
        connection.rollback()

    finally:
        close_cursor(cursor)
        close_connection(connection)

    
    return result




# Gets completed user tasks
def get_completed_tasks():


    # Initializing result as empty list
    result = []


    # Retrieving user_id
    user_id = session.get("user_id", None)


    # Opens connection and cursor
    connection = get_connection()
    cursor = open_cursor(connection)


    try:

        # Searches for tasks of specified user
        select_tasks = f"""
            SELECT task_id
                ,task
                ,priority
                ,created_time
                ,completed_time
            FROM {schema}.tasks AS t
            JOIN {schema}.user_tasks AS ut
                ON t.id = ut.task_id
            WHERE ut.user_id = %s
                AND t.completed = 1
        """


        # Searches for tasks
        cursor.execute(select_tasks, (user_id, ))


        # Retrieves results
        result = cursor.fetchall()


        connection.commit()

    
    except Exception as e:
        print(e)
        connection.rollback()

    finally:
        close_cursor(cursor)
        close_connection(connection)

    
    return result




# Creates task and stores in database
def create_task(task, priority = None):

    
    # Initializing task_id as 0
    task_id = 0

    
    # Opens connection and cursor
    connection = get_connection()
    cursor = open_cursor(connection)


    # Verifies user is logged in
    if session.get("user_id", None):

        try:

            if priority:
                # Query to insert task
                insert_task = f"""
                    INSERT INTO {schema}.tasks (
                        task
                        ,priority
                        ,created_time
                    ) VALUES (
                        %s
                        ,%s
                        ,NOW(6)
                    )
                """

                # Inserts task into tasks table
                cursor.execute(insert_task, (task, priority))


            else:
                # Query to insert task
                insert_task = f"""
                    INSERT INTO {schema}.tasks (
                        task
                        ,created_time
                    ) VALUES (
                        %s
                        ,NOW(6)
                    )
                """

                # Inserts task into tasks table
                cursor.execute(insert_task, (task, ))



            # Retrieves id of inserted task
            task_id = cursor.lastrowid


            connection.commit()
        

        except Exception as e:
            print(e)
            connection.rollback()

        finally:
            close_cursor(cursor)
            close_connection(connection)

    
    return task_id




# Creates user task mapping and stores in database
def create_task_mapping(task_id):
    

    # Retrieving user_id
    user_id = session.get("user_id", None)


    # Opens connection and cursor
    connection = get_connection()
    cursor = open_cursor(connection)

    
    # Verifies user is logged in
    if user_id:

        try:
            # Query to insert task mapping
            insert_task_mapping = f"""
                INSERT INTO {schema}.user_tasks (
                    user_id
                    ,task_id
                ) VALUES (
                    %s
                    ,%s
                )
            """


            # Inserts task mapping into user_tasks table
            cursor.execute(insert_task_mapping, (user_id, task_id))


            connection.commit()

        
        except Exception as e:
            print(e)
            connection.rollback()

        finally:
            close_cursor(cursor)
            close_connection(connection)




# Updates task by marking complete and setting completion time
def update_task_complete(task_id):

    
    # Retrieving user_id
    user_id = session.get("user_id", None)


    # Opens connection and cursor
    connection = get_connection()
    cursor = open_cursor(connection)


    # Verifies user is logged on
    if user_id:

        try:
            # Query to update task
            update_task_complete = f"""
                UPDATE {schema}.tasks
                SET completed = 1
                    ,completed_time = NOW(6)
                WHERE id = &s
            """


            # Updates task in user_tasks table
            cursor.execute(update_task_complete, (task_id, ))


            connection.commit()

        
        except Exception as e:
            print(e)
            connection.rollback()

        finally:
            close_cursor(cursor)
            close_connection(connection)
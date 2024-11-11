from services.data_service import get_connection, open_cursor, close_cursor, close_connection

from flask import session
import os


# Getting database schema from .env
schema = os.environ.get("SCHEMA")




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
                        '{task}'
                        ,{priority}
                        ,NOW(6)
                    )
                """

            else:
                # Query to insert task
                insert_task = f"""
                    INSERT INTO {schema}.tasks (
                        task
                        ,created_time
                    ) VALUES (
                        '{task}'
                        ,NOW(6)
                    )
                """


            # Inserts task into tasks table
            cursor.execute(insert_task)


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
                    {user_id}
                    ,{task_id}
                )
            """


            # Inserts task mapping into user_tasks table
            cursor.execute(insert_task_mapping)


            connection.commit()

        
        except Exception as e:
            print(e)
            connection.rollback()

        finally:
            close_cursor(cursor)
            close_connection(connection)
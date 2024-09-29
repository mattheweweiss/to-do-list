from services.data_service import get_connection, open_cursor, close_cursor, close_connection

import os
import bcrypt


# Getting database schema from .env
schema = os.environ.get("SCHEMA")


def create_account(first_name, last_name, email, password):

    query = f"""
        INSERT INTO {schema}.users (
            [first_name]
            ,[last_name]
            ,[email]
            ,[password]
        ) VALUES (
            {first_name}
            ,{last_name}
            ,{email}
            ,{bcrypt.hashpw(password, bcrypt.gensalt())}
        )
    """

    print(query)

    # connection = get_connection()
    # cursor = open_cursor(connection)

    # cursor.execute(query)

    # close_cursor(cursor)
    # close_connection(connection)
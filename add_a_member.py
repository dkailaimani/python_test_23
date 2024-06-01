import mysql.connector
from mysql.connector import errorcode

def add_member(id, name, age, trainer_id):
    try:
        # Create database connection
        db_conn = mysql.connector.connect(user='root', password='XyZ$9#1@7QwEeTy',
                                      host='localhost', database='Workout_Session')

        # Create cursor object
        with db_conn.cursor() as cursor:
            # Validation for Member ID
            cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
            existing_member = cursor.fetchone()
            if existing_member:
                print("ERROR: MEMBER ID ALREADY EXISTS!")
                return

            # Insert the new member into database
            cursor.execute("INSERT INTO Members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)",
                           (id, name, age, trainer_id))

            # Commit changes
            db_conn.commit()

            print("NEW MEMBER ADDED!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied, check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERROR: DATABASE DOES NOT EXIST!")
        else:
            print(f"Error: {err}")
    finally:
        # Closes connection
        if db_conn.is_connected():
            db_conn.close()


add_member(1, "Jimmy Chew", 20, 2)

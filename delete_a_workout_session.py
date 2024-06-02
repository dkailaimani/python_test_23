import mysql.connector

def delete_workout_session(session_id):
    try:
        # Establish database connection
        db_conn = mysql.connector.connect(user='root', password='XyZ$9#1@7QwEeTy',
            host='localhost', database='Workout_Session')

        # Create cursor object
        cursor = db_conn.cursor()

        # Validate session ID
        cursor.execute("SELECT * FROM Workout_Session WHERE session_id = %s", (session_id,))
        existing_session = cursor.fetchone()
        if not existing_session:
            print("ERROR: SESSION ID DOES NOT EXIST!")
            return

        # Delete workout session
        cursor.execute("DELETE FROM Workout_Session WHERE session_id = %s", (session_id,))

        # Commit changes
        db_conn.commit()

        print("WORKOUT SESSION DELETED!")

    except mysql.connector.Error as err:
        print(f"ERROR: {err}")

    finally:
        # Close cursor and connection
        cursor.close()
        db_conn.close()

delete_workout_session(1)

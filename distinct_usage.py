import mysql.connector

def distinct_trainers():
    try:
        # Establish database connection
        db_conn = mysql.connector.connect(user='root', password='XyZ$9#1@7QwEeTy',
                                      host='localhost', database='Workout_Session')

        # Create cursor object
        cursor = db_conn.cursor()

        # Execute SQL query using DISTINCT
        cursor.execute("SELECT DISTINCT trainer_id FROM Members")

        # Get results and print to console
        trainers = [row[0] for row in cursor.fetchall()]
        print("UNIQUE TRAINERS:", trainers)

    except mysql.connector.Error as err:
        print(f"ERROR: {err}")

    finally:
        # Close cursor and connection
        cursor.close()
        db_conn.close()

distinct_trainers()

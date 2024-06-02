import mysql.connector 

def between_age_usage(start_age, end_age):
    try:
        # Establish database connection
        db_conn = mysql.connector.connect(user='root', password='XyZ$9#1@7QwEeTy',
                                      host='localhost', database='Workout_Session')

        # Create cursor object
        cursor = db_conn.cursor()

        # Execute SQL query using BETWEEN
        cursor.execute("SELECT name, age, trainer_id FROM Members WHERE age BETWEEN %s AND %s",
                       (start_age, end_age))

        # Get results and print to console
        members_in_range = cursor.fetchall()
        print("MEMBERS IN AGE RANGE:")
        for member in members_in_range:
            print(f"Name: {member[0]}, Age: {member[1]}, Trainer ID: {member[2]}")

    except mysql.connector.Error as err:
        print(f"ERROR: {err}")

    finally:
        # Close cursor and connection
        cursor.close()
        db_conn.close()

between_age_usage(22, 24)

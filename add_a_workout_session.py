import mysql.connector

def add_a_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        # Establish database connection
        db_conn = mysql.connector.connect(user='root', password='XyZ$9#1@7QwEeTy',
                                      host='localhost', database='Workout_Session')

        # Create cursor object
        cursor = db_conn.cursor()

        # Validation for member ID
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        existing_member = cursor.fetchone()
        if not existing_member:
            print("ERROR: MEMBER ID DOES NOT EXIST!")
            return

        # Insert new workout session into database
        cursor.execute("INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)",
                       (member_id, date, duration_minutes, calories_burned))

        # Commit changes
        db_conn.commit()

        print("WORKOUT SESSION ADDED!")

    except mysql.connector.Error as err:
        print(f"ERROR: {err}")

    finally:
        # Close cursor and connection
        cursor.close()
        db_conn.close()

add_workout_session(1, '2024-05-31', 120, 770)

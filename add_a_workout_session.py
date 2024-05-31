import mysql.connector

def add_a_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        # Establish database connection
        cnx = mysql.connector.connect(user='root', password='That08er',
                                      host='localhost', database='MyCodingTempleData')

        # Create cursor object
        cursor = cnx.cursor()

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
        cnx.commit()

        print("WORKOUT SESSION ADDED!")

    except mysql.connector.Error as err:
        print(f"ERROR: {err}")

    finally:
        # Close cursor and connection
        cursor.close()
        cnx.close()

add_workout_session(1, '2024-05-31', 120, 770)

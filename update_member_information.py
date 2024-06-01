import mysql.connector

def update_member_age(member_id, new_age):
    try:
        # Establish database connection
        db_conn = mysql.connector.connect(user='root', password='XyZ$9#1@7QwEeTy',
                                      host='localhost', database='Workout_Session')

        # Create cursor object
        cursor = db_conn.cursor()

        # Check if the member exists
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        existing_member = cursor.fetchone()
        if not existing_member:
            print("ERROR: MEMBER ID DOES NOT EXIST!")
            return

        # Update member's age
        cursor.execute("UPDATE Members SET age = %s WHERE id = %s", (new_age, member_id))

        # Commit changes
        db_conn.commit()

        print("MEMBER AGE UPDATED!")

    except mysql.connector.Error as err:
        print(f"ERROR: {err}")

    finally:
        # Close cursor and connection
        cursor.close()
        db_conn.close()

update_member_age(1, 26)

import mysql.connector

def number_of_members_per_trainer():
    try:
        # Establish database connection
        db_conn = mysql.connector.connect(user='root', password='XyZ$9#1@7QwEeTy',
                                      host='localhost', database='Workout_Session')

        # Create cursor object
        cursor = db_conn.cursor()

        # Execute SQL query using COUNT and GROUP BY
        cursor.execute("SELECT trainer_id, COUNT(*) FROM Members GROUP BY trainer_id")

        # Get and print results to console
        trainer_member_counts = {row[0]: row[1] for row in cursor.fetchall()}
        print("MEMBER PER DISTINCT TRAINER:", trainer_member_counts)

    except mysql.connector.Error as err:
        print(f"ERROR: {err}")

    finally:
        # Close cursor and connection
        cursor.close()
        db_conn.close()

number_of_members_per_trainer()

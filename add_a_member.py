import mysql.connector
from mysql.connector import errorcode

def add_member(id, name, age, trainer_id):
    try:
        # Create database connection
        cnx = mysql.connector.connect(user='root', password='That08er',
                                      host='localhost', database='mycodingtempledata')

        # Create cursor object
        with cnx.cursor() as cursor:
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
            cnx.commit()

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
        if cnx.is_connected():
            cnx.close()


add_member(1, "Jimmy Chew", 20, 2)

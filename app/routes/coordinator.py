from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector
import database.connection as dbc

coordinator_bp = Blueprint('coordinator_bp', __name__, url_prefix='/coordinator')

@coordinator_bp.route('/')
def coordinator():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT CID , name , age , email, dateOfBirth FROM coordinator")
            data = cursor.fetchall()
            return render_template('coordinator.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

@coordinator_bp.route('/submit_coordinator', methods=['GET', 'POST'])
def add_coordinator():
    if request.method == 'POST':
        full_name = request.form['name']
        dateOfBirth = request.form['date_of_birth']
        date_of_birth = datetime.strptime(dateOfBirth, '%Y-%m-%d')
        today = datetime.today()
        email = generate_unique_email(full_name)
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

        try:
            connection = dbc.connect_to_db()
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("INSERT INTO coordinator (name , age , email , dateOfBirth) VALUES (%s, %s , %s , %s)",
                               (full_name, age , email , date_of_birth))
                connection.commit()
                return redirect(url_for('home_bp.home'))
        except mysql.connector.Error as error:
            print("Error inserting data into MySQL:", error)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
        return render_template('index.html')


def generate_unique_email(full_name):
    current_year = str(datetime.now().year)
    name_parts = full_name.split()
    first_name = name_parts[0]
    last_name = name_parts[-1]
    email = f"{first_name}.{last_name}.{current_year}.coo@Aiu.edu.eg"

    conn = dbc.connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM instructor WHERE email = %s", (email,))
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.close()
            conn.close()
            return email
        else:
            new_full_name = ' '.join(name_parts[:-1])
            return generate_unique_email(new_full_name)
    except mysql.connector.Error as e:
        print(f"Error checking for unique email: {e}")
        return None
    finally:
        cursor.close()
        conn.close()



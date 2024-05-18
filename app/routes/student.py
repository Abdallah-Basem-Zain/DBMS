from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
import mysql.connector
import database.connection as dbc

student_bp = Blueprint('student_bp', __name__, url_prefix='/student')


@student_bp.route('/')
def student():
    fields = []
    data = []
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM aiufield")
            fields = [row[0] for row in cursor.fetchall()]
    except mysql.connector.Error as error:
        print("Error fetching fields from MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT SID , Name , Email , NumEnrolledCourses , NumCompletedCourses , JoinDate , Field  , Level FROM courses.student;")
            data = cursor.fetchall()
    except mysql.connector.Error as error:
        print("Error fetching student data from MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

    return render_template('student.html', data=data, fields=fields)


@student_bp.route('/submit_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        full_name = request.form['full_name']
        field = request.form['field']
        email = generate_unique_email(full_name)
        join_date = datetime.now().strftime("%Y-%m-%d")
        level =  request.form['level']

        try:
            connection = dbc.connect_to_db()
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("INSERT INTO Student (name , Field , Email , JoinDate , Level ) VALUES (%s, %s , %s , %s , %s)",
                               (full_name, field, email, join_date , level))
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
    email = f"{first_name}.{last_name}.{current_year}@Aiu.edu.eg"

    conn = dbc.connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM Student WHERE Email = %s", (email,))
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

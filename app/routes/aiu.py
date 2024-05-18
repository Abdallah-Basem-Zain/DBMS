import code
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector
import database.connection as dbc

aiu_bp = Blueprint('aiu_bp', __name__, url_prefix='/aiu')

@aiu_bp.route('/')
def aiu():
    fields = []
    instructors = []
    semesters = []
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT name , id FROM aiufield")
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
            cursor.execute("SELECT name , IID FROM instructor")
            instructors = [row[0] for row in cursor.fetchall()]
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
            cursor.execute("SELECT name  , sem_ID FROM semester")
            semesters = [row[0] for row in cursor.fetchall()]
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
            cursor.execute("""
            SELECT 
    AIU_Course.code AS AIU_Code,
    AIU_Course.noOfExpStudent AS Expected_Students,
    Instructor.name AS Instructor_Name,
    AIUfield.name AS Field_Name,
    CONCAT(Semester.name, ' ', YEAR(Semester.year)) AS Semester_Info,
    Mapping.module AS Mapping_Module
FROM 
    AIU_Course
JOIN 
    Instructor ON AIU_Course.IID = Instructor.IID
JOIN 
    AIUfield ON AIU_Course.fielded = AIUfield.id
JOIN 
    Semester ON AIU_Course.SEMID = Semester.sem_ID
JOIN 
    Mapping ON AIU_Course.Mappingid = Mapping.id;
""")
            data = cursor.fetchall()
            return render_template('aiuCourses.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()



@aiu_bp.route('/submit_aiu', methods=['GET', 'POST'])
def add_aiu():
    if request.method == 'POST':
        course_code = request.form['course_code']
        NO_expected = request.form['No_expected']
        instructor = request.form['instructor'].split(" ")[1]
        field = request.form['field'].split(" ")[1]
        semester = request.form['semester'].split(" ")[1]
        try:
            connection = dbc.connect_to_db()
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("INSERT INTO aiu_course (code , noOfExpStudent , IID , fielded , SEMID) VALUES (%s, %s , %s , %s , %s)",
                               (code, NO_expected, instructor, field ,semester))
                connection.commit()
                return redirect(url_for('home_bp.home'))
        except mysql.connector.Error as error:
            print("Error inserting data into MySQL:", error)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
        return render_template('index.html')


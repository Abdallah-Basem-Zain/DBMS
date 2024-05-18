from flask import Blueprint, render_template
import mysql.connector
import database.connection as dbc

coursera_bp = Blueprint('coursera_bp', __name__, url_prefix='/coursera')

@coursera_bp.route('/')
def coursera():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select courseslug , name, organization , type , Coursecode , specialization_link , studentsenrolled , studentscomp , number_of_weeks , number_of_hours From coursera_course")
            data = cursor.fetchall()
            return render_template('coursera.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
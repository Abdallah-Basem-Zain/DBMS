from flask import Blueprint, render_template
import mysql.connector
import database.connection as dbc

license_bp = Blueprint('license_bp', __name__, url_prefix='/license')

@license_bp.route('/')
def license():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT lid , startDate , endDate , numOfstudents FROM License ")
            data = cursor.fetchall()
            return render_template('license.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

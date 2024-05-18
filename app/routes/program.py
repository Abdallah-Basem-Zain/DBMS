from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector
import database.connection as dbc

program_bp = Blueprint('program_bp', __name__, url_prefix='/program')

@program_bp.route('/')
def program():
    try:
        connection = dbc.connect_to_db()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM courseprogram")
            data = cursor.fetchall()
            return render_template('program.html', data=data)
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


@program_bp.route('/submit_program', methods=['GET', 'POST'])
def add_program():
    if request.method == 'POST':
        name = request.form['name']
        learner_link = request.form['learner_link']
        admin_link = request.form['admin_link']
        try:
            connection = dbc.connect_to_db()
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("INSERT INTO courseprogram (name , learner_link , admin_link) VALUES (%s, %s , %s)",
                               (name, learner_link, admin_link))
                connection.commit()
                return redirect(url_for('home_bp.home'))
        except mysql.connector.Error as error:
            print("Error inserting data into MySQL:", error)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
        return render_template('index.html')


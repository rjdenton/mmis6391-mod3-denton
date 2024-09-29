from flask import render_template, request, redirect, url_for
from .db import get_db_connection

db_config = {
    'user': 'phk51m847pg19v0w',
    'password': 'wdvedu7x318sbqzo',
    'host': 'arfo8ynm6olw6vpn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    'database': 'tpobmwnvw9nqjzlz'
}


def init_routes(app):

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

def init_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/services')
    def services():
        return render_template('services.html')

    @app.route('/products')
    def products():
        return render_template('products.html')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            animal_type = request.form['animal_type']
            message = request.form['comment']

            # Call a function to insert the data into your database
            insert_contact_info(name, email, animal_type, message)

            # Redirect after form submission
            return redirect(url_for('home'))

        return render_template('contact.html')

def insert_contact_info(name, email, animal_type, message):
    # Get database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert the contact information into the database
    query = """
    INSERT INTO contacts (name, email, animal_type, message)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, animal_type, message))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

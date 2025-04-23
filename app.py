from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import mysql.connector
from mysql.connector import Error

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

# MySQL database connection configuration
def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Update with your MySQL host
            user='root',       # Update with your MySQL username
            password='Family01@', # Update with your MySQL password
            database='mlproject_db'  # Update with your MySQL database name
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Function to create table if not exists
def create_table():
    connection = create_db_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS predictions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        gender VARCHAR(20),
        race_ethnicity VARCHAR(50),
        parental_level_of_education VARCHAR(50),
        lunch VARCHAR(20),
        test_preparation_course VARCHAR(20),
        reading_score FLOAT,
        writing_score FLOAT,
        predicted_math_score FLOAT,
        prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

create_table()

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    render_template('home.html')
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")

        # Save input data and prediction result to MySQL database
        connection = create_db_connection()
        if connection is not None:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO predictions 
            (gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score, predicted_math_score)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            record = (
                request.form.get('gender'),
                request.form.get('ethnicity'),
                request.form.get('parental_level_of_education'),
                request.form.get('lunch'),
                request.form.get('test_preparation_course'),
                float(request.form.get('writing_score')),
                float(request.form.get('reading_score')),
                results[0]
            )
            cursor.execute(insert_query, record)
            connection.commit()
            cursor.close()
            connection.close()

        return render_template('home.html',results=results[0])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
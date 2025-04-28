# MLProject: Student Math Score Prediction

## Project Overview
MLProject is a comprehensive machine learning solution designed to predict student mathematics scores based on demographic and academic indicators. This end-to-end pipeline encompasses data ingestion, preprocessing, model training, evaluation, and deployment via a Flask web application, with persistent storage of predictions in a MySQL database.

## Key Features
- Robust data preprocessing and exploratory data analysis on student performance datasets.
- Implementation and evaluation of multiple regression algorithms including Linear Regression, Random Forest, XGBoost, CatBoost, among others.
- User-friendly Flask web interface for real-time prediction of student math scores.
- Integration with MySQL for storing prediction records and facilitating data management.
- Modular and scalable codebase structured for maintainability and extensibility.

## Installation Instructions

### Prerequisites
- Python 3.7+
- MySQL Server (configured and running)

### Setup Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MLProject
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure MySQL database:
   - Create a database named `mlproject_db`.
   - Update database connection parameters in `app.py` as necessary.

## Usage Guide

### Running the Application
Launch the Flask application by executing:
```bash
python app.py
```
Access the web interface at `http://localhost:5000` to input student data and obtain predicted math scores.

## Data Description
The dataset includes the following features:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score
- Target Variable: Math Score

Extensive exploratory data analysis was conducted to understand feature distributions and correlations.

## Model Development and Evaluation
- Data preprocessing involved one-hot encoding for categorical variables and standard scaling for numerical features.
- Multiple regression models were trained and assessed using metrics such as Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared (R²).
- Ensemble methods like CatBoost and XGBoost demonstrated superior predictive performance.

## Project Structure
- `app.py`: Flask application entry point.
- `src/components/`: Modules for data ingestion, transformation, and model training.
- `src/pipeline/`: Training and prediction pipeline implementations.
- `notebook/`: Jupyter notebooks for exploratory data analysis and model training.
- `artifacts/`: Serialized models, preprocessors, and datasets.
- `requirements.txt`: Python package dependencies.
- `setup.py`: Project packaging and metadata.

## Author
Sumit  
Email: sumit.gupta.14486@gmail.com

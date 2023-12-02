# stockmarketpred.py
from flask import Flask, render_template, request, Blueprint
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

stock_app = Blueprint('stock_app', __name__, template_folder='templates')


# Load the trained machine learning model
model = joblib.load('stock_model.pkl')  # Adjust the model file name if needed
X_scaler = joblib.load('X_scaler.pkl')
y_scaler = joblib.load('y_scaler.pkl')

def cleanup(df):
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

# Define the preprocessing function
def preprocess_input(data):
    df = pd.DataFrame(data, index=[0])
    df = cleanup(df)
    
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y', errors='coerce')
    
    #Feature Engineering
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['DayofWeek'] = df['Date'].dt.dayofweek
    df['DayofYear'] = df['Date'].dt.dayofyear
    df['Open-Delta'] = df['Open'] - df['Open'].shift(1)
    df['Volume-Delta'] = df['Shares Traded'] - df['Shares Traded'].shift(1)
    df['Turnover-Delta'] = df['Turnover (Crores)'] - df['Turnover (Crores)'].shift(1)
    
    # Additional Features
    df['Open-Percent-Change'] = (df['Open'] - df['Open'].shift(1)) / df['Open'].shift(1) * 100
    df['Volume-Percent-Change'] = (df['Shares Traded'] - df['Shares Traded'].shift(1)) / df['Shares Traded'].shift(1) * 100
    df['Turnover-Percent-Change'] = (df['Turnover (Crores)'] - df['Turnover (Crores)'].shift(1)) / df['Turnover (Crores)'].shift(1) * 100

    window_size = 5
    df['Open-Moving-Avg'] = df['Open'].rolling(window=window_size).mean()
    df['Volume-Moving-Avg'] = df['Shares Traded'].rolling(window=window_size).mean()
    df['Turnover-Moving-Avg'] = df['Turnover (Crores)'].rolling(window=window_size).mean()

    #df = pd.get_dummies(df, columns=['DayofWeek', 'Month'], drop_first=True)

    df.drop(columns=['Date'], inplace=True)
    columns = ['Turnover-Percent-Change', 'Open-Percent-Change', 'Volume-Percent-Change', 'Shares Traded', 'Open-Delta', 'DayofYear',
       'Turnover (Crores)', 'Year', 'Volume-Moving-Avg', 'Open-Moving-Avg', 'Open', 'Turnover-Moving-Avg', 'Volume-Delta', 
       'Turnover-Delta', 'Month']
    df = pd.DataFrame(X_scaler.transform(df[columns]), columns=columns)
    df.fillna(0, inplace=True)
    df = cleanup(df)
    
    return df

# Define a route for the stock app home page
@stock_app.route('/')
def stock_home():
    return render_template('stockmarketpred.html')  # Add a specific homepage for stock app

# Define a route for handling the form submission
@stock_app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = {
            #'Gender': request.form['gender'],
            'Date' : request.form['date'],
            'Open' : request.form['open'],
            'Shares Traded' : request.form['shares_traded'],
            'Turnover (Crores)' : request.form['turnover'],
            # Add other form fields here corresponding to your dataset columns
        }
        print("Got it!")
        # Preprocess the input data
        input_data = preprocess_input(data)
        
        print(data,"\n",input_data)

        # Make predictions using the loaded model
        prediction = model.predict(input_data)
        prediction = y_scaler.inverse_transform(prediction)
        print("Ans:",prediction,type(prediction))
        
        #Convert given floating point hours into HH:MM:SS format
        answer = f"High: {prediction[0, 0]:.3f};    Low: {prediction[0, 1]:.3f};    Closing: {prediction[0, 2]:.3f}"

        # Pass the prediction to the HTML template
        return render_template('stockmarketpred.html', prediction=answer)

if __name__ == '__main__':
    stock_app.run(debug=True)

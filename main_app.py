#main_app.py
from flask import Flask, render_template
from noshow_classification import noshow_app
from appointment_time_prediction import appointment_app
from stockmarketpred import stock_app

app = Flask(__name__, template_folder='templates')

# Register the blueprints for each sub-app
app.register_blueprint(noshow_app, url_prefix='/noshow')
app.register_blueprint(appointment_app, url_prefix='/appointment')
app.register_blueprint(stock_app, url_prefix='/stock')

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
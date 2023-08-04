from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# this will give the entry point to use it
application = Flask(__name__)

app = application


# Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
      # Will redirect to a webscreen where you input text boxes and shit 
      return render_template('home.html')
    else:
       data = CustomData(
        Ram=int(request.form.get('Ram')),
        Ssd=int(request.form.get('Ssd')),
        Ghz=float(request.form.get('Ghz')),
        Graphics=request.form.get('Graphics'),
        Resolution=request.form.get('Resolution')
       )
       pred_df = data.get_data_as_data_frame()
       print(pred_df)

       predict_pipeline = PredictPipeline()
       results = predict_pipeline.predict(pred_df)
    return render_template('home.html', results = results[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

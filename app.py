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
        TypeName=request.form.get('Typename'),
        Company=request.form.get('Company'),
        OpSys=request.form.get('Opsys'),
        Ram=int(request.form.get('Ram')),
        Memory=request.form.get('Memory'),
        Ghz=float(request.form.get('Ghz')),
        Touchscreen=bool(request.form.get('Touchscreen')),
        IPS=bool(request.form.get('IPS')),
        is_4K=bool(request.form.get('is_4K')),
        Processor=request.form.get('Processor'),
        Gpu_Brand=request.form.get('Gpu_Brand'),
        Resolution=request.form.get('Resolution')
       )
       pred_df = data.get_data_as_data_frame()
       print(pred_df)

       predict_pipeline = PredictPipeline()
       results = predict_pipeline.predict(pred_df)
    return render_template('home.html', results = results[0])

if __name__ == '__main__':
    app.run(debug=True, port=8080)

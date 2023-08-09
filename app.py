from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import joblib as joblib
from flask_cors import CORS


from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# this will give the entry point to use it
application = Flask(__name__)
app = application
CORS(app)
# Route for a home page


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    data = request.get_json()

    data_dict = {
        "memory/ram": [data["Ram"]],
        "Ssd": [data["Ssd"]],
        "Ghz": [data["Ghz"]],
        "graphics_quality": [data["Graphics"]],
        "resolution": [data["Resolution"]],
    }

    # Creating the KNN model to give a simiarltiy recommendation

#    from sklearn.neighbors import KNeighborsRegressor

    pred_df = pd.DataFrame(data_dict)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    # Assuming results is a list of predictions
    prediction_result = float(results[0])

    return jsonify({"prediction": prediction_result})


# Goodbye yellow brick road
app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

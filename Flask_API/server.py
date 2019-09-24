import numpy as np
from flask import Flask, request, json, jsonify
import pickle
import version as v

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/linear_reg', methods=['POST'])
def predict():
    try:
        #Get Output
        data = request.get_json(force=True)
        # Make prediction using model loaded from disk
        prediction = model.predict([[np.array(data['exp'])]])
        # Get the output
        output = {'prediction': prediction[0]}
        # Response Codes
        response = app.response_class(response=json.dumps(output),
                                      status=200,
                                      mimetype='application/json')
        # Response.headers['Content-Type'] = 'application/json'
        return response

    except Exception as e:
        error = {"error": "error_occurred", "reason": str(e)}
        response = app.response_class(response=json.dumps(error),
                                      status=500,
                                      mimetype='error/application')
        return response


@app.route('/version', methods=['GET'])
def get_app_version():
    return jsonify({'app': 'This is a test for flask package', 'version': v.__version__})


app.run(port=1080, debug=False)

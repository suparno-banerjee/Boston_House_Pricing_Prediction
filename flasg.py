import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd
import flasgger
from flasgger import Swagger    # For a better UI

app = Flask(__name__)
Swagger(app)

## Load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

#route to home page
@app.route('/')
def home():
    return render_template('home.html')

# route to prediction model
@app.route('/predict', methods=['POST'])
def predict():

    """Let's predict Boston House Prices
    This is using docstrings for specifications
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true

    responses:
        200:
            description: The output Values

    """
    df_test = pd.read_csv(request.files.get("file"))
    x = len(df_test)
    final_input = scalar.transform(np.array(df_test).reshape(x,-1))
    print(final_input)
    output = regmodel.predict(final_input)
    return " The Predicted Price of the house is: " + str(output)


if __name__ =='__main__':
    app.run(debug=True)
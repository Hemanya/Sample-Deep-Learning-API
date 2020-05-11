# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:24:53 2020

@author: heman
"""

from flask import Flask, jsonify, request
import sqlite3
import json
import pandas as pd
from keras.models import Sequential, model_from_json
from keras.layers import Dense
from tensorflow import keras

app = Flask(__name__)

@app.route('/')
def main():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    query = '''SELECT * FROM models'''
    c = cur.execute(query)
    models = c.fetchall()
    response = []
    for model in models:
        response.append({'id':model[0], 'timestamp':model[1], 'accuracy':model[2]})
        
    return(jsonify(response))

# 'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#'BMI', 'DiabetesPedigreeFunction', 'Age'
#http://127.0.0.1:5000/predict?Model=1&Pregnancies=6&Glucose=148&BloodPressure=72&SkinThickness=35&Insulin=0&BMI=33.6&DiabetesPedigreeFunction=0.627&Age=50'
@app.route('/predict')
def predict():
    X = []
    model = request.args.get('Model',None)
    X.append(int(request.args.get('Pregnancies', None)))
    X.append(int(request.args.get('Glucose', None)))
    X.append(int(request.args.get('BloodPressure', None)))
    X.append(int(request.args.get('SkinThickness', None)))
    X.append(int(request.args.get('Insulin', None)))
    X.append(float(request.args.get('BMI', None)))
    X.append(float(request.args.get('DiabetesPedigreeFunction', None)))
    X.append(int(request.args.get('Age', None)))
    df_X = pd.DataFrame([X], columns =['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'] )
    model_name = str(model) + '.json'
    weight_name = str(model) + '.h5'
    json_file = open(model_name,'r')
    
    loaded_model_json = json_file.read() 
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(weight_name)
    
    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    predict = loaded_model.predict_classes(df_X)[0][0]
    if predict == 1:
        predict = "Prediction: Diabetic"
    else:
        predict = "Prediction: Not Diabetic"
    return(predict)

@app.route('/test')
def test():
    return(request.args.get('arg1',None))

if __name__ == '__main__':
    app.run(threaded=False)
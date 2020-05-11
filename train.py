# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:28:05 2020

@author: heman
"""

from numpy import loadtxt
from keras.models import Sequential, model_from_json
from keras.layers import Dense
import sqlite3
#######################Model Here
import pandas as pd
# load the dataset
dataset = pd.read_csv('pima-indian-diabetes.csv').head(n = 600)
# split into input (X) and output (y) variables
X = dataset.iloc[:,0:8]
y = dataset.iloc[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
accuracy = int(accuracy*100)

#######################Model Ends

# Connect to database and query the models
conn = sqlite3.connect('database.db')
query = '''INSERT INTO models(metric) VALUES(?)'''
cur = conn.cursor()
cur.execute(query,(accuracy,))
conn.commit()#There is actually no need for this. Will remove in future git commits
conn.close()
# Connect to DB and select the latest model ID and save it using that ID.
conn = sqlite3.connect('database.db')
query = '''SELECT max(id) from models'''
cur = conn.cursor()
cur.execute(query)
save_id = cur.fetchall()
conn.close()
#Save the model and model weights
name = str(save_id[0][0])
model_name = name +'.json'
weight_name = name + '.h5'
model_json = model.to_json()
with open(model_name, 'w') as json_file:
    json_file.write(model_json)
model.save_weights(weight_name)



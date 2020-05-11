# Sample-Deep-Learning-API
A deep learning API which stores model versions and predicts according to the model selected

1. Create a database (and a table which stores model ID, timestamp when the model was trained and the accuracy) by running create_db.py
2. Use the train.py file to train your models. Everytime you run train.py file, following happens:
  a. A new entry is added into the table "models" storing the time at which the model was trained, and the accuracy along with the model        ID.
  b. The model is saved as <ID>.json with the weights being saved as <ID>.h5. The project already has 2 entries in the database and 2          models saved.
3. Run main.py to run the flask application. Before running, set FLASK_DEBUG as False.
4. The Flask application is now running. There are 2 urls in the urls.txt file.Run the first url on your browser to get the models
5. Run the second url to predict. You can play with the parameters.

Notes:
1. Future Improvement 1: Instead of a Get call for prediction, use Post.
2. Future Improvement 2: Make a UI and beautify.
3. The model currently uses prima indian diabetes dataset to predict diabetes. Note that this API can be used for any model. The only change that needs to be done is in train.py. 

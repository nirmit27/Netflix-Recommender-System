import pymongo
import configparser
import pandas as pd
from flask import Flask, render_template, request, url_for


# Fetching credentials
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
connection_string = cfg.get('MDB', 'connection_string')


# Connecting to MongoDB
client = pymongo.MongoClient(connection_string)
db = client['recommender_system']


# Fetching the datasets ...
# Similarity Scores

collection1 = db['sim_scores']
cursor1 = collection1.find()

sim_scores = pd.DataFrame(list(cursor1))
sim_scores.drop("_id", axis=1, inplace=True)
sim_scores.set_index('Movie_ID', inplace=True)

# Movie Titles

collection2 = db['netflix_data']
cursor2 = collection2.find()

movie_titles = pd.DataFrame(list(cursor2))
movie_titles.drop("_id", axis=1, inplace=True)
movie_titles.set_index('Movie_Id', inplace=True)


# App configuration
app = Flask(__name__)

# Routes ... 

# Home

@app.route('/')
def index():
    return render_template('index.html')

# Model 1

@app.route('/model1')
def model1():
    return render_template('model1.html')

# Model 2

@app.route('/model2')
def model2():
    return render_template('model2.html')

# Model 3

@app.route('/model3')
def model3():
    return render_template('model3.html')

# Model 4

@app.route('/model4')
def model4():
    return render_template('model4.html')


# Driver code
if __name__=="__main__":
    app.run(debug=True)

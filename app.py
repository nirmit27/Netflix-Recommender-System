import pymongo
import configparser
import pandas as pd


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


# Driver code
if __name__=="__main__":

    # print(sim_scores.head())
    print(movie_titles.head())

# TODO: make a song recommender
# TODO: def function(): that recommends events, based on a song
#   >> then expand this to recommend an event based on a user's ID

import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data_imports = ['data/users.json', 'data/events.json']

# open and read json files
with open(data_imports[0]) as users_data:
    users_json = json.load(users_data)

with open(data_imports[1]) as events_data:
    events_json = json.load(events_data)

users_df = pd.DataFrame(users_json["objects"])
events_df = pd.DataFrame(events_json["objects"])

# removing duplicates
# print(events_df.duplicated(subset='event_name').sum())
# events_df = events_df.drop_duplicates(subset='event_name')
# print(events_df.duplicated(subset='event_name').sum())

# cleaning the text
""" *******************************************************
*    Title: How to Build a Recommendation System in Python
*    Author: Natassha Selvaraj
*    Date: 12 Apr 2023
*    Code version: 1.0
*    Availability: https://365datascience.com/tutorials/how-to-build-recommendation-system-in-python/#4
* 
    ****************************************************** """
def clean_text(author):
    result = str(author).lower()
    return(result.replace(' ',''))

# clean the text calling clean_text()
users_df['user_fav_song'] = users_df['user_fav_song'].apply(clean_text)
users_df['user_fav_genre'] = users_df['user_fav_genre'].apply(clean_text)
users_df['user_fav_artist'] = users_df['user_fav_artist'].apply(clean_text)
events_df['event_genre'] = events_df['event_genre'].apply(clean_text)
# TODO: continue from 365datascience.com -->

users_df['user_fav_artist']

# print(users_df.head(25))
# print(events_df.head(25))
print(events_df.info())

# extracting necessary info from data
users_features = ['user_fav_genre', 'user_fav_artist', 'user_fav_song']
events_features = ['event_name', 'event_location', 'event_genre', 'date']

user_songs = users_df[users_features].copy()
events = events_df[events_features].copy()

# combine datasets
# user_songs.loc[:, 'combined_songs'] = user_songs['user_fav_genre'] + ' ' + user_songs['user_fav_artist'] + ' ' + user_songs['user_fav_song']
events.loc[:, 'combined_events'] = events['event_name'] + ' ' + events['event_location'] + ' ' + events['event_genre'] + ' ' + events['date']

print(user_songs)
print(events)

# creating countvectorizer
cv = CountVectorizer()

# vectorize each dataframe
songs_cv = cv.fit_transform(user_songs['combined_songs'])
events_cv = cv.fit_transform(events['combined_events'])

# calculate cosine similarity vector of each item in data
songs_sim = cosine_similarity(songs_cv)
events_sim = cosine_similarity(events_cv)



# # event recommender - based on event genre
# def event_recommender(eventGenre):
#     eventGenre = clean_text(eventGenre)

#     events_df['index'] = range(len(events_df))

#     # grab all indexes of events with matching genre
#     event_indexes = events_df[events_df.event_genre == eventGenre]['index'].values[0]

#     # get the cosine sim compared to index of inputted genre and then sort by sim. in desc
#     sim_events = list(enumerate(events_sim[event_indexes]))
#     # x[1] sets index to 1 as generated data starts at 1
#     sim_events_sorted = sorted(sim_events, key=lambda x: x[1], reverse=True)
    
#     # extract indexes into a list
#     sim_events_indexes = [i[0] for i in sim_events_sorted]

#     # make new dataframe to contain all recommended events
#     rec_events_df = events_df.iloc[sim_events_indexes][events_features]
#     # rec_events_df = events_df.iloc[sim_events_indexes][['event_name', 'event_location', 'event_genre', 'date']]

#     # reset the index of rec events (so that their original index is not printed)
#     rec_events_df = rec_events_df.reset_index(drop=True)

#     # return the top x events
#     return rec_events_df.head(5)

# # print(event_recommender('Techno'))
# # print(event_recommender('House'))
# print(event_recommender('Hard Rock'))

# # event recommender, taking user's favourite genre
# def user_genre_recommender(userID):
#     user = users_df.loc[users_df['ID'] == str(userID)].iloc[0]

#     fav_genre = user['user_fav_genre']
#     print(f"user[{userID}]'s name : {user['user_name']}")
#     print(f"user[{userID}]'s fav genre : {fav_genre}")
#     recommended_events = event_recommender(fav_genre)

#     return recommended_events

# userid = input("user id to generate recommended events : ")
# print(user_genre_recommender(userid))
    

# # TODO: make a song recommender
# # TODO: def function(): that recommends events, based on a song
# #   >> then expand this to recommend an event based on a user's ID
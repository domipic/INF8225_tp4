import json
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

tfidf = TfidfVectorizer()
sid = SentimentIntensityAnalyzer()

all_lyrics = []

for root, dirs, files in os.walk("../lemmatized_lyrics/database"):
    for name in files:
        infile = open(root + "/" + name, "r")
        lyrics = infile.read().replace('\n', ' ').split("_")[0]
        all_lyrics.append(lyrics)

fitted = tfidf.fit_transform(all_lyrics)

tfidf_stats = fitted.toarray()

words = []

for prop in tfidf.vocabulary_:
    words.append(prop)

scores = []

for song in tfidf_stats:
    total_positivity = 0
    total_neutrality = 0
    total_negativity = 0
    for i in range(0, len(song)):
        total_positivity = total_positivity + song[i]*(sid.polarity_scores(words[i]))["pos"]
        total_neutrality = total_neutrality + song[i]*(sid.polarity_scores(words[i]))["neu"]
        total_negativity = total_negativity + song[i]*(sid.polarity_scores(words[i]))["neg"]
    scores.append({
        "pos":total_positivity,
        "neu":total_neutrality,
        "neg":total_negativity
    })
    
outfile = open("sentiment_scores_tfidf", "w")
json.dump(scores, outfile)

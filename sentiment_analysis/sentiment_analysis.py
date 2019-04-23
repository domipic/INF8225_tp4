from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import os
import json

all_lyrics = []

for root, dirs, files in os.walk("../lyrics-master/database"):
    for name in files:
        if "lemmatized" in name:
            infile = open(root + "/" + name, "r")
            lyrics = infile.read().replace('\n', ' ').split("_")[0]
            all_lyrics.append(lyrics)

tokenized_lyrics = []

#for lyric in all_lyrics:
 #   tokenized_lyrics.append(word_tokenize(lyric))

sid = SentimentIntensityAnalyzer()

sentiments = []

for lyric in all_lyrics:
    print (lyric)
    ss = sid.polarity_scores(lyric)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    
    print(ss)
    sentiments.append(ss)
    print()

outfile = open("sentiment_scores", "w")

json.dump(sentiments, outfile)
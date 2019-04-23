from collections import Counter
import json
import io
import os
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

counter = CountVectorizer()

all_lyrics = []
counts = {}

for root, dirs, files in os.walk("../lemmatized_lyrics/database"):
    for name in files:
        if "lemmatized" in name:
            infile = open(root + "/" + name, "r")
            lyrics = infile.read().replace('\n', ' ').split("_")[0]
            all_lyrics.append(lyrics)

fitted = counter.fit_transform(all_lyrics)

counts["feature_names"] = counter.get_feature_names()
counts["counts"] = fitted.todense().tolist()

outfile = open("tf_counts", "w")
print(all_lyrics)
json.dump(counts, outfile)

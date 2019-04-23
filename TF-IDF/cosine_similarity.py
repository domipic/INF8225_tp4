import json
import os
import codecs
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

tfidf = TfidfVectorizer()

all_lyrics = []

for root, dirs, files in os.walk("../lemmatized_lyrics/database"):
    for name in files:
        if "lemmatized" in name:
            infile = open(root + "/" + name, "r")
            lyrics = infile.read().replace('\n', ' ').split("_")[0]
            all_lyrics.append(lyrics)

fitted = tfidf.fit_transform(all_lyrics)
cosine_similarities = cosine_similarity(fitted)
print(cosine_similarities)

outfile = codecs.open("cosine_similarities", 'w', encoding='utf-8')

cosine_similarities_list = cosine_similarities.tolist()
json.dump(cosine_similarities_list, outfile, separators=(',', ':'), sort_keys=True, indent=4)

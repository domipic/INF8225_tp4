import json
import os
import numpy as np

def find_song_and_artist(index):
    iterated = 0
    for root, dirs, files in os.walk("../lyrics-master/database"):
        for name in files:
            if "_lemmatized" in name:
                if iterated == index:
                    print(name, root.split("/")[-2])
                    return name, root.split("/")[-2]
                else:
                    iterated = iterated + 1

similarities_json = json.load(open("../TF-IDF/cosine_similarities", "r"))
sentiments_json = json.load(open("../sentiment_analysis/sentiment_scores", "r"))

similarities = []

for song in similarities_json:
    for score in song:
        if (score < 0.99):
            similarities.append(score)
        else:
            similarities.append(0)

similarities = np.array(similarities)

max_similarities = similarities.argsort()[-50:][::-1]
max_similarities = [v for i, v in enumerate(max_similarities) if i % 2 == 0]

left_song_indexes = []
right_song_indexes = []

for index in max_similarities:
    left_song_indexes.append(int(((index - (index % float(len(similarities_json))))/float(len(similarities_json)))))
    right_song_indexes.append(int(index % float(len(similarities_json))))

pairs = []

print(left_song_indexes)
print(right_song_indexes)
for i in range(0, len(left_song_indexes)):
    left_song, left_artist = find_song_and_artist(left_song_indexes[i])
    right_song, right_artist = find_song_and_artist(right_song_indexes[i])
    if left_song.split("_")[0].lower() not in right_song.split("_")[0].lower() and right_song.split("_")[0].lower() not in left_song.split("_")[0].lower():
        pairs.append({
            "similarity":similarities[int(max_similarities[i])],
            "left": {
                "song":left_song.split("_")[0],
                "artist":left_artist
            },
            "right":{
                "song":right_song.split("_")[0],
                "artist":right_artist
            }
        })


outfile = open("top_5_similar_songs", "w")
json.dump(pairs[0:5], outfile)



positive_scores = []
negative_scores = []

for song in sentiments_json:
    positive_scores.append(song["pos"])
    negative_scores.append(song["neg"])

positive_scores = np.array(positive_scores)
negative_scores = np.array(negative_scores)

max_pos = positive_scores.argsort()[-5:][::-1]
max_neg = negative_scores.argsort()[-5:][::-1]

top_positives = []
top_negatives = []


for i in range(0, 5):
    song, artist = find_song_and_artist(max_pos[i])
    top_positives.append({
        "score":positive_scores[int(max_pos[i])],
        "song":{
            "title":song.split("_")[0],
            "artist":artist
        }
    })
    song, artist = find_song_and_artist(max_neg[i])
    top_negatives.append({
        "score":negative_scores[int(max_neg[i])],
        "song":{
            "title":song.split("_")[0],
            "artist":artist
        }
    })

outfile = open("top_5_positives", "w")
json.dump(top_positives, outfile)

outfile = open("top_5_negatives", "w")
json.dump(top_negatives, outfile)
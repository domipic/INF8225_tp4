import json

similarities = json.load(open("../TF-IDF/cosine_similarities", "r"))
sentiments = json.load(open("../sentiment_analysis/sentiment_scores", "r"))

diffs = []

for i in range(0, len(similarities)):
    song_diffs = []
    for j in range(0, len(similarities)):
        diff = {
            "similarity" : similarities[i][j],
            "neg_diff" : abs(sentiments[i]["neg"] - sentiments[j]["neg"]),
            "neu_diff" : abs(sentiments[i]["neu"] - sentiments[j]["neu"]),
            "pos_diff" : abs(sentiments[i]["pos"] - sentiments[j]["pos"])
        }
        song_diffs.append(diff)
    diffs.append(song_diffs)


outfile = open("sentiment_diffs_and_similarity", "w")

json.dump(diffs, outfile)
    


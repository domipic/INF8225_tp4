import json
import matplotlib.pyplot as plt
import math

cosine_similarities = json.load(open("../TF-IDF/cosine_similarities", "r"))

plt.matshow(cosine_similarities)
plt.colorbar()
plt.savefig("matrice_sim.png", dpi=300)

plt.clf()


data = json.load(open("../sentiment_analysis/sentiment_diffs_and_similarity", "r"))

diff_matrix = []


for song in data:
    diffs = []
    for song2 in song:
        diffs.append(1 - math.sqrt(dict(song2)["pos_diff"] ** 2 + dict(song2)["neg_diff"] ** 2) )
    diff_matrix.append(diffs)



plt.matshow(diff_matrix)
plt.colorbar()
plt.savefig("matrice_emotional_diffs.png", dpi=300)
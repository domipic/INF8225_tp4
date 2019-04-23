import json
import matplotlib.pyplot as plt

data = json.load(open("../sentiment_analysis/sentiment_scores", "r"))

pos = []
neu = []
neg = []

for song in data:
    pos.append(song["pos"])
    neu.append(song["neu"])
    neg.append(song["neg"])

pos.sort(reverse=True)
neu.sort(reverse=True)
neg.sort(reverse=True)


plt.plot(pos)
plt.ylabel('Score de positivité')
plt.xlabel('Index des chansons (triées par positivité décroissante)')
plt.show()
plt.savefig("pos_graph.png", dpi=300)

plt.clf()

plt.plot(neu)
plt.ylabel('Score de neutralité')
plt.xlabel('Index des chansons (triées par neutralité décroissante)')
plt.show()
plt.savefig("neu_graph.png", dpi=300)

plt.clf()

plt.plot(neg)
plt.ylabel('Score de négativité')
plt.xlabel('Index des chansons (triées par négativité décroissante)')
plt.show()
plt.savefig("neg_graph.png", dpi=300)
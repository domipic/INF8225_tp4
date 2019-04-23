# INF8225_tp4

Travail effectué par Dominique Piché, Jean-Guillaum Langlois et Reph Mombrun

## Prérequis

- Python3.6
- Installation Windows de TreeTagger
- librairies python: numpy, pandas, matplotlib, sklearn, treetaggerwrapper, nltk

## Ordre d'exécution
L'ordre d'exécution des scripts est important, puisqu'un script produit généralement des données qu'un script subséquent utilisera.
Il est important d'exécuter les scripts à partir d'un shell placé dans leur sous-dossier, sinon leurs résultats ne seront pas stockés aux bons endroits.
Les sorties (sauf les paroles lemmatisées) sont stockées sous format json dans des fichiers sans extension.

1. lemmatization/lemmatizer.py

Produit des paroles lemmatisées dans une arborescence identique à celle des paroles originales.

2. TF-IDF/tf-vectorizer.py, TF-IDF/cosine_similarity.py

tf-vectorizer.py produit un fichier contenant tous les mots découverts, et le compte pour chaque chanson de la fréquence d'apparition de chacun de ces mots.

cosine_similarity.py produit une matrice de similarités cosinus entre les chansons.

3. sentiment_analysis/sentiment_analysis.py, sentiment_analysis/sentiment_analysis_tfidf.py

sentiment_analysis.py produit un vecteur d'objets contentant les scores de sentiments positifs, neutres et négatifs pour chaque chanson.

sentiment_analysis_tfidf.py produit ce même vecteurs d'objets, mais avec la considération que la contribution de chaque mot au scores émotionnelles est modulée par l'importance relative de ce mot (tf-idf) pour chaque chanson. De plus, ces sentiments ne sont pas normalisés, faisant en sorte qu'une chanson plus longue de même émotion qu'une chanson plus courte sera évaluée comme ayant de l'émotion plus forte.

4. sentiment_analysis/sentiment_similiraty_diff_generator.py

Ce script génère une matrice pour les similarités entre les émotions présentes dans toutes les chansons (en prenant la différence des scores de positivité, de négativité et de neutralité).

5. result_generator/result_table_generator.py, result_generator/result_graph_generator.py, result_generator/graph_matrix_sim_and_sentiments.py

result_table_generator.py génère des listes d'objets contenant les top 5 chansons les plus similaires, les plus positives et négatives. result_graph_generator.py produit des graphiques montrant les scores émotionnels des chansons en ordre décroissant. graph_matrix_sim.py produit des représentations visuelles de la matrice de similarité cosinus du vocabulaire et de la matrice de proximité émotionnelle des chansons.

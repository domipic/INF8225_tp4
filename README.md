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

Produit des paroles lemmatisées dans une arborescence similaire

2. TF-IDF/tf-vectorizer.py, cosine_similarity.py
3. sentiment_analysis/sentiment_analysis.py, sentiment_analysis/sentiment_analysis_tfidf.py
4. sentiment_analysis/sentiment_similiraty_diff_generator.py
5. result_generator/result_table_generator.py, result_generator/result_graph_generator.py, result_generator/graph_matrix_sim_and_sentiments.py

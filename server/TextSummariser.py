from Preprocess import tokenize, preprocess, clean_summary
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import re


def vectorize(clean_sentences):
    embeddings_dict = {}

    with open("glove.6B.50d.txt", 'r', encoding="utf8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], "float32")
            embeddings_dict[word] = vector

    sentence_vectors = []
    for sentence in clean_sentences:
        if len(sentence) != 0:
            vector = sum([embeddings_dict.get(word, np.zeros((50,)))
                          for word in sentence.split()])/(len(sentence.split()))
        else:
            vector = np.zeros((50,))
        sentence_vectors.append(vector)

    return sentence_vectors


def text_rank(data):
    """Applies text_rank algorithm on text passed as a parameter and returns a summary"""

    sentences = tokenize(data)
    l = len(sentences)
    clean_sentences = preprocess(sentences)
    sentence_vectors = vectorize(clean_sentences)
    # Computing Similarity Matrix
    s_mat = np.zeros([l, l])

    for i in range(l):
        for j in range(l):
            if i != j:
                s_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(
                    1, 50), sentence_vectors[j].reshape(1, 50))[0, 0]

    # Applying PageRank Algorithm - To Calculate Sentence Scores
    graph = nx.from_numpy_array(s_mat)
    sentence_scores = nx.pagerank(graph)

    ranked_sentences = sorted(
        ((sentence_scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    summary = []
    x = round(l * 0.2)
    for i in range(x):
        summary.append(ranked_sentences[i][1])
    print(l)
    print(x)
    return clean_summary(summary)

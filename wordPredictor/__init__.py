# -*- coding: utf-8 -*-

import re
import unidecode
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


########################################################################################################################


def ngrams(string, n=3):
    string = re.sub(r'[,-./]|\s',r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])

    return [''.join(ngram) for ngram in ngrams]


def cleanWord(txt):
    txt = txt.lower().strip()
    txt = unidecode.unidecode(txt)
    txt = re.sub(r'[^a-z0-7]+', ' ', txt)

    return txt


def makeModel(textTrainList, threshold=0):
    textTrainList = [cleanWord(x) for x in textTrainList]

    vectorizer = TfidfVectorizer(min_df=threshold, analyzer=ngrams)
    vector_matrix = vectorizer.fit_transform(textTrainList)

    return vector_matrix, vectorizer


def predWord(word, wordsList, vectorizer, vector_matrix, idList = None, top_rank=5):
    word = cleanWord(word)
    strigX = vectorizer.transform([word]).toarray()

    cosine_similarities = linear_kernel(strigX, vector_matrix).flatten()
    related_indices = cosine_similarities.argsort()[:-(top_rank + 1):-1]
    scores = list(cosine_similarities[related_indices])

    res = [wordsList[x] for x in related_indices]
    ids = [idList[x] for x in related_indices if idList] if idList is not None else list(related_indices)

    dataOut = {'words': res, 'keys': ids, 'distances': scores}
    print(dataOut)
    return dataOut


########################################################################################################################

if __name__ == "__main__":
    print()
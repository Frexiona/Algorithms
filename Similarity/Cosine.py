import math
import nltk
import copy
import numpy

from nltk.corpus import stopwords
from collections import Counter
from nltk.corpus import stopwords
from nltk import data

data.path.append('D:\\Software\\NltkData\\nltk_data')

def getCorpus(url):
    raw_text = open(url , "r")
    texts = raw_text.read().split('\n')
    raw_text.close()

    return texts

def tokenlizeText(texts):
    items_list = list()
    for j in range(len(texts)):
        items_list.append(nltk.word_tokenize(texts[j]))

    return items_list

def removePuncStopwords(items_list):
    for z in range(len(items_list)):
        items_list[z] = [w.lower() for w in items_list[z] if w.isalnum()]
        items_list[z] = [i for i in items_list[z] if (i not in stopwords.words('english'))]

    return items_list

def getItemList(items_list):
    words = list()
    for sentence in items_list:
        for word in sentence:
            words.append(word)
    count = Counter(words)

    unique_items = list(count.keys())
    return unique_items

def calTfIdf(items_list):
    #TF
    words = list()
    items_tf = [[]for i in range(len(items_list))]
    count_list = 0
    for sentence in items_list:
        # TF
        items_tf[count_list].append(dict(Counter(sentence)))
        count_list += 1
        for word in sentence:
            words.append(word)

    # DF
    items_df = dict(Counter(words))

    unique_items = list(items_df.keys())

    # N(The number of items in the corpus)
    N = len(words)

    # IDF
    items_idf = dict()
    for each in items_df.keys():
        items_idf[each] = math.log(N / items_df[each])

    # TF-IDF
    items_tfidf = [[] for i in range(len(items_list))]
    dict_tfidf = dict()
    count_tfidf = 0
    for sentence_dict in items_tf:
        for item in sentence_dict[0].keys():
            if item in items_df.keys():
                dict_tfidf[item] = sentence_dict[0][item] * items_idf[item]
        items_tfidf[count_tfidf].append(copy.deepcopy(dict_tfidf))
        dict_tfidf.clear()
        count_tfidf += 1

    # Make matrix of tfidf
    matrix_tfidf = list()
    temDict_matrix = dict()
    count_matrix = 0
    for eachdict in items_tfidf:
        for eachword in unique_items:
            if(eachword not in list(items_tfidf[count_matrix][0].keys())):
                temDict_matrix[eachword] = 0
            else:
                temDict_matrix[eachword] = items_tfidf[count_matrix][0][eachword]
        matrix_tfidf.append(copy.deepcopy(temDict_matrix))
        temDict_matrix.clear()
        count_matrix += 1

    return matrix_tfidf


def getCosine(dict_s1 , dict_s2):
    numerator = sum(dict_s1[eachword] * dict_s2[eachword] for eachword in list(dict_s1.keys()))
    print(numerator)
    denominator = math.sqrt(sum(x * x for x in list(dict_s1.values()))) * math.sqrt(sum(y * y for y in list(dict_s2.values())))
    print(denominator)
    if denominator == 0:
        return 0.0

    cosine  = round(float(numerator) / float(denominator) , 3)

    return cosine

text = getCorpus("F:\\UCD\\Courses\\Text Analytics\\Lec5\\P5\\c1.txt")
items_list = tokenlizeText(text)
items_list = removePuncStopwords(items_list)
unique_items = calTfIdf(items_list)
print(list(unique_items[0].values()))
print(numpy.array(list(unique_items[0].values())))
vector1 = numpy.array(list(unique_items[1].values()))
vector2 = numpy.array(list(unique_items[2].values()))
print(numpy.sum(numpy.square(vector1 - vector2)))
cosine1 = getCosine(unique_items[0] , unique_items[1])
cosine2 = getCosine(unique_items[0] , unique_items[2])
cosine3 = getCosine(unique_items[1] , unique_items[2])
print(cosine1 , cosine2 , cosine3)
# print(cosine_similarity(unique_items[0] , unique_items[1]))
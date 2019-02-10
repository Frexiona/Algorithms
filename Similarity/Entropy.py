import nltk
import math

from nltk.corpus import stopwords
from nltk import data
from collections import Counter

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

def arrayToList(words_list):
    word_list2 = list()
    for i in range(len(words_list)):
        for j in words_list[i]:
            word_list2.append(str(j))

    return word_list2

def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    print(probs)
    return (-sum(p * math.log2(p) for p in probs))

texts_spam = getCorpus("F:\\UCD\\Courses\\Text Analytics\\Lec4\\P4\\text2_spam.txt")
items_list_spam = tokenlizeText(texts_spam)
items_list_spam = removePuncStopwords(items_list_spam)
words_list = arrayToList(items_list_spam)
count = Counter(words_list)
print(count)
e = entropy(words_list)
print(e)
import nltk
import operator
import math

from nltk.corpus import stopwords
from nltk import data
from collections import Counter



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

def removeRepItems(items_list):
    words = set()
    for k in range(len(items_list)):
        for each in items_list[k]:
            words.add(each)

    words_list = list(words)

    return words_list

def arrayToList(words_list):
    word_list2 = list()
    for i in range(len(words_list)):
        for j in words_list[i]:
            word_list2.append(str(j))

    return word_list2

class PML(object):

    def countNumItems(self , words_list):

        return len(words_list)

    def countNum1Item(self , words_list , key):
        count = Counter(words_list)
        DF_of_word = dict(count)
        value = DF_of_word[key]

        return value

    def countNumAdjaItems(self , words_list):
        adja_items = [[] for a in range(len(words_list) - 1)]
        for i in range(len(adja_items)):
            adja_items[i].append(words_list[i])
            adja_items[i].append(words_list[i+1])

        count_adjaitems = list()
        for k in range(len(adja_items)):
            count = 0
            for j in range(1 , len(words_list)):
                if(words_list[j - 1] == adja_items[k][0] and words_list[j] == adja_items[k][1]):
                    count += 1
            count_adjaitems.append(count)

        count_adja_items = dict()
        for h in range(len(adja_items)):
            count_adja_items[str(adja_items[h])] = count_adjaitems[h]

        return count_adja_items

    def calPMI(self , words_list):
        count_adja_items = self.countNumAdjaItems(words_list)
        N = self.countNumItems(words_list)

        keys_of_count_adja_items = list()
        for k in count_adja_items.keys():
            keys_of_count_adja_items.append(k)

        pmi_scores = dict()
        for i in range(1 , len(words_list)):
            Cw1 = self.countNum1Item(words_list , words_list[i - 1])
            Cw2 = self.countNum1Item(words_list , words_list[i])
            key = [words_list[i - 1] , words_list[i]]
            Cw1_w2 = count_adja_items[str(key)]

            pmi_scores[str(key)] = math.log2(Cw1_w2 * N) / (Cw1 * Cw2)

        return sorted(pmi_scores.items() , key = operator.itemgetter(1))


if __name__ == '__main__':
    url = "F:\\UCD\\Courses\\Text Analytics\\Lec4\\P4\\text.txt"
    texts = getCorpus(url)
    items_list = tokenlizeText(texts)
    items_list = removePuncStopwords(items_list)
    words_list = arrayToList(items_list)
    pmi = PML()
    items = pmi.calPMI(words_list)
    for i in range(10):
        print(items[i])
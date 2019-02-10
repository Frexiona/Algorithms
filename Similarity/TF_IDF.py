import nltk
import math

from collections import Counter
from nltk.corpus import stopwords
from nltk import data

data.path.append('D:\\Software\\NltkData\\nltk_data')

raw_text = open("F:\\UCD\\Courses\\Text Analytics\\Lec4\\P4\\text.txt" , "r")
texts = []
for i in raw_text.readlines():
    texts.append(i)
raw_text.close()

items_list = []
for j in range(len(texts)):
    items_list.append(nltk.word_tokenize(texts[j]))

# Remove the punctuation and the outlier in items
for z in range(len(items_list)):
    items_list[z] = [w.lower() for w in items_list[z] if w.isalnum()]
    items_list[z] = [i for i in items_list[z] if(i not in stopwords.words('english'))]

words = set()
wordcloud_list1 = list()
for k in range(len(items_list)):
    for each in items_list[k]:
        words.add(each)
        wordcloud_list1.append(each)

words_list = list(words)

print(words_list)
print(wordcloud_list1)

words_freq = [[] for g in range(len(words))]
words_count = 0

for j in range(len(items_list)):
    for word in words_list:
        if word not in items_list[j]:
            words_freq[words_count].append(0)
            words_count += 1
        else:
            words_freq[words_count].append(items_list[j].count(word))
            words_count += 1
    words_count = 0

for c in range(1,11):
    print('C' + str(c) , end = ' ')

print()

print_count = 0
for w in words_list:
    if print_count < 10:
        print(w , end = ' ')
        print(words_freq[print_count])
        print_count += 1
    else:
        break

# DF:
counter = Counter(wordcloud_list1)
words_DF = dict(counter)
print(words_DF)

# IDF
words_IDF = dict()
for item in words_DF:
    words_IDF[item] = math.log(10 / words_DF[item])

print(words_IDF)

# TF-IDF:
for c in range(1,11):
    print('C' + str(c) , end = ' ')
print()

print_count2 = 0
for w in words_list:
    if print_count2 < 10:
        print(w , end = ' ')
        for num in words_freq[print_count2]:
            print(num * words_IDF[w] , end =' ')
        print_count2 += 1
        print()
    else:
        break

# wordFreq based on tf-idf
tf_idf_list = list()
df_idf_weight = 0;
for key in words_DF:
    df_idf_weight = words_DF[key] * words_IDF[key]
    for i in range(int(2 * df_idf_weight)):
        tf_idf_list.append(key)

for i in tf_idf_list:
    print(i,end = ' ')
'''
items_list = nltk.word_tokenize(text)

# Remove the punctuation
words = [w.lower() for w in items_list if w.isalnum()]

filted_stopwords_items = [i for i in words if(i not in stopwords.words('english'))]

print(filted_stopwords_items)

count = Counter(filted_stopwords_items)
print(count.most_common(10))

# Count the frequency of words
tfDict = {}
count = 1
for words in filted_stopwords_items:
    tfDict[words] = count
    count += 1

# https://www.cnblogs.com/koliverpool/p/6791614.html
sortedtfDict = sorted(tfDict.items() ,key = operator.itemgetter(1) , reverse= True )

'''
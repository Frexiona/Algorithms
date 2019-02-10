import nltk

from nltk.corpus import stopwords
from nltk import data

data.path.append('D:\\Software\\NltkData\\nltk_data')

def getCorpus(url):
    raw_text = open(url , "r")
    texts = raw_text.read().split('\n')
    raw_text.close()

    return texts

def calJeccardDis(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    jeccard_index = float(len(set1 & set2) / len(set1 | set2))
    jeccard_dis = round(1 - jeccard_index , 2)

    return jeccard_dis

def calDiceDis(sentence1 , sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    dice_coefficient = float((2 * len(set1 & set2)) / (len(set1) + len(set2)))
    dice_dis = round(dice_coefficient , 2)

    return dice_dis

text = getCorpus("F:\\UCD\\Courses\\Text Analytics\\Lec5\\P5\\text.txt")
for i in range(len(text) - 1):
    for j in range(i + 1 , len(text)):
        dice_distance = calDiceDis(text[i] , text[j])
        print("[ Sentence" , str(i+1) , "," , "Sentence" , str(j+1) , "]' Dice Coefficient : " , dice_distance)
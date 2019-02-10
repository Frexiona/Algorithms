import copy
import random
import distance

from random import choice

a = ["#Cyberspiracy","#Cybersecurity","#InfoSec","#Hacking","#Malware","#Spam","https://buff.ly/2R4NSwv"," 🌟 https://buff.ly/2R2umRi","🌟 https://buff.ly/2R4kCpJ","🌟 https://buff.ly/2R7QBpb","🌟 https://buff.ly/2q2ZzbF"]

normal_tweets1 = "I love Dave La Chapelle’s art."
normal_tweets2 = "Here's why claims that Democrats or George Soros are funding a caravan of migrants from Honduras are false."
normal_tweets3 = "Mnuchin to Travel to Saudi Arabia to Reinforce Ties, Despite Uproar Over Khashoggi Killing."
normal_tweets4 = "Surveillance footage caught a man falling down a flight of steps because he couldn’t take his eyes off his phone in China."
normal_tweets5 = "After Saudi Arabia announced economic austerity measures in 2015 to offset low oil prices and control a widening budget gap, McKinsey & Company, the consulting firm, measured the public reception of those policies."

print(len(normal_tweets1))
print(len(normal_tweets2))
print(len(normal_tweets3))
print(len(normal_tweets4))
print(len(normal_tweets5))

spam = [[] for j in range(20)]
for i in range(20):
    temp = copy.deepcopy(normal_tweets1)
    for p in range(random.randint(5,10)):
        temp += choice(a)
    spam[i].append(temp)

d = [[] for r in range(5)]
for f in range(20):
    ans1 = distance.levenshtein(normal_tweets1 , str(spam[f]))
    d[0].append(ans1)
    ans2 = distance.levenshtein(normal_tweets2, str(spam[f]))
    d[1].append(ans2)
    ans3 = distance.levenshtein(normal_tweets3, str(spam[f]))
    d[2].append(ans3)
    ans4 = distance.levenshtein(normal_tweets4, str(spam[f]))
    d[3].append(ans4)
    ans5 = distance.levenshtein(normal_tweets5, str(spam[f]))
    d[4].append(ans5)

print(d)
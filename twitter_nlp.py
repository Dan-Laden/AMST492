#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################
print("Main File")
import time
start_time = time.time()

import nltk #ref doc: http://www.nltk.org/howto/index.html
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk import FreqDist
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import string #ref doc: https://docs.python.org/3.3/library/string.html?highlight=string#module-string
import re #ref doc: https://docs.python.org/3/library/re.html#re.ASCII
import random


stoplist = set(stopwords.words('english'))#set of all stopwords in english thanks to nltk

#########################
# Function definitions

def twitter_sorter(twitter_feed):
    sorted_list = []
    idea = ""
    size_limit = 0
    for line in twitter_feed:
        if not idea:
            idea = line
            size_limit = len(line.split(";"))
            continue
        else:
            line = line.split(";")
            #print(len(line))
            if len(line) == size_limit:
                pass
            else:
                continue
            #text,favourites,retweets,username,date
            post = [line[4], line[3], line[2], line[0], line[1]]
            sorted_list.append(post)

    return sorted_list


#########################
# Main code
paris = open("paris.csv", 'r')
greta = open("greta.csv", 'r')
#username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink

p_list = twitter_sorter(paris)
g_list = twitter_sorter(greta)

print(p_list[0])
print(len(p_list))

print(g_list[2])
print(len(g_list))

#End of main code
#########################
seconds = round(time.time() - start_time)
minutes = 0
hours = 0
if seconds > 60:
    minutes = int(seconds/60)
    seconds = seconds - (minutes * 60)
if minutes > 60:
    hours = int(minutes/60)
    minutes = minutes - (hours * 60)
print("--- %s hours ---\n--- %s minutes ---\n--- %s seconds ---" % (hours, minutes, seconds))
#########################
#resources used for code so far
#
# http://www.algorithm.co.il/blogs/programming/python/cheap-language-detection-nltk/
#########################

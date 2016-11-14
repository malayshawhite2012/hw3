# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) , 
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
# requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import nltk
from nltk.book import text2
import random

# import nltk
# nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize


tokens_original_text= text2
for elm in tokens_original_text:
	print (elm, end = " ")

tokens = text2[:150]
print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","PRP":" a preposition"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "PRP": .1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))
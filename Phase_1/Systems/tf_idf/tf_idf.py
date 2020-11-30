import os
import re
import math
import pandas as pd
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


stop_words = set(stopwords.words('english')) 


# Computes term frequency for the word
def comput_TF (dictt, listt):
	tfdict = {}
	lenn = len (listt)
	for word, count in dictt.items():
		tfdict[word] = count / float (lenn)
	return tfdict



def sett(lst):
	s = set()
	for item in lst:
		# print (lst)
		s.add(item)
	return s
def pre_process(text):
	
	# lowercase
	text=text.lower()
	
	#remove tags
	text=re.sub("&lt;/?.,*?&gt;"," &lt;&gt; ",text)
	
	# remove special characters and digits
	text=re.sub("(\\d|\\W)+"," ",text)
	
	return text


# Computes inverse document frequncy version 1
def compute_IDF (listt):
	idfdict = {}
	N = len (listt)
	idfdict = dict.fromkeys (listt[1].keys(),0)
	for doc in listt:
		for word, val in doc.items():
			if val > 0:
				idfdict[word] == 1

	for word, val in idfdict.items():
		if float(val) > 0:
			idfdict[word] = math.log (N / float(val))
		else:
			idfdict[word] = 0;

	return idfdict


# Computes inverse document frequncy version 2
def computeIDF (vocab, mas_listt):
	idcf = {}
	N = len(mas_listt)
	idcf = dict.fromkeys(vocab,0)

	for key in idcf:

		for i in range(1,len(mas_listt)):
			if key in mas_listt[i]:
				idcf[key] += 1

		idcf[key] = idcf[key] / N		

	return idcf


# Computes TF-IDF values 
def TFIDF (tfdict, idfs):
	tfidf = {}
	for word, val in tfdict.items():
		tfidf[word] = val * idfs[word]
	return tfidf





mas_listt = [[]]
vocab = []
word_dict = {}
ii = 1
# for i in os.listdir('/home/dhaval/MTP/tf_idf/input'):
for root, subFolder, files in os.walk('./input'):
	for item in files:
		fileNamePath = str(os.path.join(root,item))
		print (fileNamePath)
		ff = open (fileNamePath,'r')
		lines = ff.readlines()
		listt = []
		for ll in lines:
			ll = pre_process(ll)
			spll = ll.split(" ")
			listt = listt + spll
		print ("------" + str(ii) + "------")
		ii+= 1
		print (len (listt))
		filtered_listt = [] 
	  
		for w in listt: 
			if w not in stop_words: 
				filtered_listt.append(w) 
		vocab = list(set(vocab) | set(filtered_listt))
		mas_listt.append(filtered_listt)
# vocab.remove("   ")
for i in range(1,len(mas_listt)):
	word_dict[i] = dict.fromkeys(vocab,0)
	for word in mas_listt[i]:
		word_dict[i][word] += 1

	word_dict[i] = comput_TF (word_dict[i], mas_listt[i])

df = pd.DataFrame(word_dict)

temp = [{}]

for key in word_dict:
	temp.append(word_dict[key])


idfs = computeIDF (vocab, mas_listt)


it = 1;
for key in word_dict:
	word_dict[it] = TFIDF (word_dict[it], idfs)
	it += 1

df = df.max(axis=1)
df = df.sort_values(ascending=False)
print (df)

df.to_csv('results.csv', sep=',')
print ("DONE")
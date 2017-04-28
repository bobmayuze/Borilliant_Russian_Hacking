import sys
import csv
from collections import defaultdict

inputFile = sys.argv[1]
output = sys.argv[2]
output2 = sys.argv[3]
output3 = sys.argv[4]
file = open(output, 'w')
outputFile2 = open(output2, 'wb')
outputFile3 = open(output3, 'wb')

columns = defaultdict(list)

with open(inputFile) as input:
	reader = csv.DictReader(input)
	for row in reader:
		for (k,v) in row.items():
			columns[k].append(v)
			
wordDict = {}
			
for text in columns["Full Text"]:
	words = text.split(' ')
	for word in words:
		if word.startswith("http") or word == "RT":
			continue
		word = ''.join(c for c in word if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#")
		if word == '':
			continue
		if word in wordDict:
			wordDict[word] = wordDict[word] + 1
		else:
			wordDict[word] = 1
		file.write(word + ' ')
		
hashtags = {}
for hashtagString in columns["Hashtags"]:
	hashtagList = hashtagString.split(" ")
	for hashtag in hashtagList:
		hashtag = ''.join(c for c in hashtag if c not in "[],' ").lower()
		if hashtag == "":
			continue
		if hashtag in hashtags:
			hashtags[hashtag] = hashtags[hashtag] + 1
		else:
			hashtags[hashtag] = 1

hashtagList = []
for key in hashtags:
	hashtagList.append((key, hashtags[key]))
hashtagList = sorted(hashtagList, key=lambda tup: tup[1])

wordList = []
for key in wordDict:
	wordList.append((key, wordDict[key]))
wordList = sorted(wordList, key=lambda tup: tup[1], reverse=True)

wr = csv.writer(outputFile2, quoting=csv.QUOTE_ALL)
for hashtag in hashtagList:
	newRow = [hashtag[0], hashtag[1]]
	wr.writerow(newRow)
	
wr = csv.writer(outputFile3, quoting=csv.QUOTE_ALL)
for word in wordList:
	newRow = [word[0], word[1]]
	wr.writerow(newRow)

file.close()
outputFile2.close()
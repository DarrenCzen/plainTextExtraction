import re
import nltk
import json


stopIndicator = 'Stop'
indicator = '-----'

keywords = ['Constant declarations' ]

data = open('example1.txt', 'r', encoding="utf-8").readlines()
content = []

prevLine = ''
newList = []

for line in data:
	if line.strip() != '':
		newList.append(line)

for lineNumber in range(0,len(newList)):
	if indicator in newList[lineNumber] and stopIndicator not in prevLine:
		topic = prevLine
		topicInfoList = []
		currentPosition = lineNumber + 1
		while(indicator not in newList[currentPosition]):
			topicInfoList.append(newList[currentPosition])
			currentPosition += 1

		topicInfo = ''
		for x in range(0,len(topicInfoList) - 1):
			topicInfo += topicInfoList[x]

		tempDict = {}
		tempDict['name'] = topic
		tempDict['info'] = topicInfo

		content.append(tempDict)


	prevLine = newList[lineNumber]

with open('test.json', 'w+') as fout:
    json.dump(content , fout)
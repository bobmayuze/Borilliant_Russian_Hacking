import sys
import json
import csv
import glob

input = sys.argv[1]
output = sys.argv[2]

outputFile = open(output, 'wb')
wr = csv.writer(outputFile, quoting=csv.QUOTE_ALL)

firstRow = ["Time Created", "Screen Name", "Follower Count", "Full Text", "Location", "Hashtags", "Mentions", "Platform"]

wr.writerow(firstRow)

jsonFiles = glob.glob(input + "/*.json")

jsonFiles.sort()

for file in jsonFiles:
	dataFile = open(file)
	inputJson = dataFile.read()
	
	jsonArr = inputJson.split('\n')

	i = 0
	
	for tweet in jsonArr:

		if tweet == "":
			continue

		else: 
			tweet = json.loads(jsonArr[i])

			newRow = []

			newRow.append(tweet["created_at"])

			newRow.append(tweet["user"]["screen_name"].encode("utf-8").strip())

			newRow.append(tweet["user"]["followers_count"])

			newRow.append(tweet["text"].encode("utf-8").strip())

			if tweet["user"]["location"] != None:
				newRow.append(tweet["user"]["location"].encode("utf-8").strip())
			else:
				newRow.append("")

			hashtags = []
			for hashtag in tweet["entities"]["hashtags"]:
				hashtags.append(hashtag["text"].encode("utf-8").strip())
			newRow.append(hashtags)

			mentions = []
			for user in tweet["entities"]["user_mentions"]:
				mentions.append(user["name"])
			newRow.append(mentions)
			
			platforms = ["iPad", "iPhone", "Android", "Twitter Web Client", "TweetDeck", "Mobile Web", "ifttt", "The Social Jukebox"]
			for platform in platforms:
				if platform in tweet["source"]:
					newRow.append(platform)
					break

			wr.writerow(newRow)

			i += 1

	dataFile.close()
	
outputFile.close()
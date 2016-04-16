from __future__ import division
import csv

arrayNegative = []
arrayPositive = []
arrayPhrases = []
arrayPhrasesWithFreq = []

with open("AllPhrases", "r") as ins:
    for line in ins:
        lastIndex = line.rfind(':')
        str1 = line[:lastIndex]
        str1.strip()
        arrayPhrases.append(str1)
        arrayPhrasesWithFreq.append(line)
        
with open("../../data/partition/validate/yelp_restaurants_reviews_positive.csv", "r") as f0:
    ins = csv.DictReader(f0)
    for line in ins:
        text = line['text']
        arrayPositive.append(text)

with open("../../data/partition/validate/yelp_restaurants_reviews_negative.csv", "r") as f1:
    ins = csv.DictReader(f1)
    for line in ins:
        text = line['text']
        arrayNegative.append(text)

numMatches = 0 
for j in range(len(arrayPositive)):
    matches = False
    for i in range(len(arrayPhrases)):
	    w = arrayPhrases[i]

	    if arrayPositive[j].find(w) > -1:
	        matches = True
	        break
	        
    if matches == True:
        numMatches += 1
        
print "Accuracy = " + str(numMatches) + "/" + str(len(arrayPositive)) + " = " + str(numMatches/len(arrayPositive))             
                        
print "Phrase \t\t\t\t Positive \t\t Negative"
for i in range(len(arrayPhrases)):
    w = arrayPhrases[i]

    positiveMatches = 0;
    for j in range(len(arrayPositive)):
        if arrayPositive[j].find(w) > -1:
            positiveMatches += 1
            
    negativeMatches = 0;
    for j in range(len(arrayNegative)):
        if arrayNegative[j].find(w) > -1:
            negativeMatches += 1
    
    print arrayPhrases[i] + "\t\t\t" + str(positiveMatches) + "/" + str(len(arrayPositive)) + "\t\t\t" + str(negativeMatches) + "/" + str(len(arrayNegative))
    #print str(positiveMatches/len(arrayPositive)) + "\t\t" + str(negativeMatches/len(arrayNegative))
    	  
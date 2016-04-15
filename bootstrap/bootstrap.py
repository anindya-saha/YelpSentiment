# vim tabstop=8 expandtab shiftwidth=4 softtabstop=4

import subprocess
import sys
import os
import re
import threading
import time
import random

reviewCollection = []
reviewsNew = []
iterCollection = []

arrayPhrases = []
arrayPhrasesNFreq = []
threshold = 15

iterate = True
iter_num = 1
index = 1

path1 = "data/partition/train/"
unlabeled_reviews = os.listdir(path1)
ln_count = 0
randomCollectionFiles = []
collection_count = 0
specificity_threshold = 0.2

threadLock = threading.Lock()
threads = []
MAX_THREADS = 5
WAIT_TIME = 1  #for thread to be available

if not os.path.exists("results"):
    os.makedirs("results")
if not os.path.exists("aux_files"):
    os.makedirs("aux_files")
if not os.path.exists("nv_files"):
    os.makedirs("nv_files")

with open("nv_files/rankReviewsNGramsFileN", "w") as ins2:
    ins2.write("great place:39")

open("results/reviewCollection.txt", "w").close()
open("results/phraseDictionary", "w").close()
open("results/logfile", "w").close()
open("nv_files/rankReviewsNGramsFileAux", "w").close()
open("aux_files/grepResults.txt", "w").close()
open("aux_files/grepResults_t1.txt", "w").close()
open("aux_files/grepResults_t2.txt", "w").close()
open("aux_files/grepResults_t3.txt", "w").close()
open("aux_files/grepResults_t4.txt", "w").close()
open("aux_files/grepResults_t5.txt", "w").close()
open("aux_files/grepResults_reviews.txt", "w").close()
open("aux_files/randomCollection.txt", "w").close()

flog = open("results/logfile", "w", 0)

class searchThread (threading.Thread):
    def __init__(self, threadID, name, reg, phrase):
        threading.Thread.__init__(self)
	self.threadID = threadID
	self.name = name
	self.reg = reg
	self.phrase = phrase
    def run(self):
        global collection_count
        global ln_count
	global index
	global iter_num
        global arrayPhrases
        global arrayPhrasesNFreq

        print str(self.threadID) + self.reg
        print str(self.threadID) + "collection_count_prev:" + str(collection_count)
	print >> flog, str(self.threadID) + self.reg
        print >> flog, str(self.threadID) + "collection_count_prev:" + str(collection_count)

        grepFileName = "aux_files/grepResults_t" + str(self.threadID) + ".txt"
        print str(self.threadID) + grepFileName
        print str(self.threadID) + "begin search"
        print >> flog, str(self.threadID) + grepFileName
        print >> flog, str(self.threadID) + "begin search"
	collection_hit_count = 0
        fg = open(grepFileName, "w")
        for tw_file in unlabeled_reviews:
            file0 = os.path.join(path1, tw_file)
            reader = csv.DictReader(file0)
            for row in reader:
                line = row['text']
                if re.search(self.reg, line, re.IGNORECASE):
                    collection_count = collection_count + 1
		    collection_hit_count = collection_hit_count + 1
                    print >> fg, line.rstrip()

	fg.close()
			
        print str(self.threadID) + "collection_count_new:" + str(collection_count)
        print str(self.threadID) + "collection_hit_count:" + str(collection_hit_count)
        print >> flog, str(self.threadID) + "collection_count_new:" + str(collection_count)
        print >> flog, str(self.threadID) + "collection_hit_count:" + str(collection_hit_count)
        
        arrayPhrasesNFreq.append(self.phrase + ':' + str(collection_hit_count))
        arrayPhrases.append(self.phrase)
        f = open("results/phraseDictionary", "a")
        f.write(self.phrase + ':' + str(collection_hit_count))
        f.write('\n')
        f.close()
        
	threadLock.acquire()
        #subprocess.check_call(["sh", "copy_grep_results.sh", "aux_files/grepResults.txt", grepFileName])
	print str(self.threadID) + 'only retain diff for analysis'            
        print >> flog, str(self.threadID) + 'only retain diff for analysis'            
        #find diff
        with open(grepFileName, "r") as twfile:
            for twt in twfile:
                if twt not in iterCollection:
                    reviewsNew.append(twt)
                    #add diff to current collection
                    iterCollection.append(twt)
            
        #save only diff in file
        #open("aux_files/grepResults.txt", "w").close()
        with open('aux_files/grepResults.txt', "a") as twfile:
            for twt in reviewsNew:
                twfile.write("%s" % twt)
                     
        reviewsNew[:] = []
                
        open(grepFileName, "w").close()
                
        threadLock.release()
        threads.remove(self)
	    

while iterate == True:

    #read rankReviewsNGramsFileN
    #use up to threshold and call grep for each not already in dict.
    with open("nv_files/rankReviewsNGramsFileN", "r") as ins:
        for line in ins:
            line = line.rstrip()
            lastIndex = line.rfind(':')
            str1 = line[:lastIndex]
            freq = line[(lastIndex + 1):]
            if (int(freq) < threshold or str1 in arrayPhrases):
                if str1 in arrayPhrases:
                    index = arrayPhrases.index(str1)
                    arrayPhrasesNFreq[index] = line
                continue    

            print "sThread"+str(len(threads)+1)
            print >> flog, "sThread"+str(len(threads)+1)
            print "sThread"+str(len(threads)+1) + str1
            print >> flog, str1
		    
            print "sThread"+str(len(threads)+1) + ": " + str1
            print >> flog, str1
            reg = str1

	        #add phrase and frequency
            #search phrase
            print "sThread"+str(len(threads)+1) + 'add phrase, search reviews'
            print >> flog, 'add phrase, search reviews'

            #wait until thread finishes
            while len(threads) == MAX_THREADS:
		        time.sleep(WAIT_TIME)

            sThread = searchThread(len(threads)+1, "sThread"+str(len(threads)+1), reg, str1)
            threads.append(sThread)
            sThread.start()
    	
        for t in threads:
            t.join()
        
    #extract reviews text
    #print 'reviews text'
    #print >> flog, 'reviews text'
    #subprocess.check_call(["node", "reviewTexts.js"])
            
    #rank and add to rankReviewsNGramsFileN; add reviews not already in set
    print 'rank phrases'
    subprocess.check_call(["node", "rankReviewsNGrams.js"])
    print 'filter phrases'
    subprocess.check_call(["node", "preFilter.js"])
    v = raw_input()

    with open("nv_files/rankReviewsNGrams", "r") as ins1:
        with open("nv_files/rankReviewsNGramsFileAux", "w") as ins2:
            for line1 in ins1:
                ins2.write(line1)
                print line1
                print >> flog, line1
                                
    #backup iteration files
    directory = "results/iter" + str(iter_num)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    for twt in iterCollection:
        if twt not in reviewCollection:
            reviewCollection.append(twt)
            
    iterCollection[:] = []         
    
    open("nv_files/rankReviewsNGrams", "w").close()
    open("nv_files/rankReviewsNGramsFull", "w").close()

    directory = "results/iter" + str(iter_num)
    subprocess.check_call(["sh", "backup_iteration_files.sh", directory])
    
    open("aux_files/grepResults.txt", "w").close()
    open("aux_files/grepResults_reviews.txt", "w").close()
    
    iter_num = iter_num + 1
    
    open("nv_files/rankReviewsNGramsFileN", "w").close()

    with open("nv_files/rankReviewsNGramsFileAux", "r") as ins1:
        with open("nv_files/rankReviewsNGramsFileN", "w") as ins2:
            for line1 in ins1:
                ins2.write(line1)
        
    open("nv_files/rankReviewsNGramsFileAux", "w").close()


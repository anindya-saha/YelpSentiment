arrayNegativePhrases = []
arrayPositivePhrases = []
arrayPositivePhrasesWithFreq = []
arrayNegativePhrasesWithFreq = []

with open("PositivePhrases", "r") as ins:
    for line in ins:
        lastIndex = line.rfind(':')
        str1 = line[:lastIndex]
        str1.strip()
        arrayPositivePhrases.append(str1)
        arrayPositivePhrasesWithFreq.append(line)
        
with open("NegativePhrases", "r") as ins:
    for line in ins:
        lastIndex = line.rfind(':')
        str1 = line[:lastIndex]
        str1.strip()
        arrayNegativePhrases.append(str1)
        arrayNegativePhrasesWithFreq.append(line)
        
f = open("PositivePhrasesFiltered", "w")
for phrase in arrayPositivePhrases:
    if phrase not in arrayNegativePhrases:
        indexP = arrayPositivePhrases.index(phrase)
        f.write(arrayPositivePhrasesWithFreq[indexP])
f.close()

f = open("NegativePhrasesFiltered", "w")
for phrase in arrayNegativePhrases:
    if phrase not in arrayPositivePhrases:
        indexP = arrayNegativePhrases.index(phrase)
        f.write(arrayNegativePhrasesWithFreq[indexP])
f.close()
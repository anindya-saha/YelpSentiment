arrayNegativeNgrams = []
arrayPositiveNgrams = []
arrayPositiveNgramsWithFreq = []
arrayNegativeNgramsWithFreq = []

with open("positiveNgrams", "r") as ins:
    for line in ins:
        lastIndex = line.rfind(':')
        str1 = line[:lastIndex]
        str1.strip()
        arrayPositiveNgrams.append(str1)
        arrayPositiveNgramsWithFreq.append(line)
        
with open("negativeNgrams", "r") as ins:
    for line in ins:
        lastIndex = line.rfind(':')
        str1 = line[:lastIndex]
        str1.strip()
        arrayNegativeNgrams.append(str1)
        arrayNegativeNgramsWithFreq.append(line)
        
f = open("positiveNgramsFiltered", "w")
for ngram in arrayPositiveNgrams:
    if ngram not in arrayNegativeNgrams:
        indexP = arrayPositiveNgrams.index(ngram)
        f.write(arrayPositiveNgramsWithFreq[indexP])
f.close()

f = open("negativeNgramsFiltered", "w")
for ngram in arrayNegativeNgrams:
    if ngram not in arrayPositiveNgrams:
        indexP = arrayNegativeNgrams.index(ngram)
        f.write(arrayNegativeNgramsWithFreq[indexP])
f.close()
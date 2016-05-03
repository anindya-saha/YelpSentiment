


Generating Ngrams:

For generation of Positive Ngrams, go to NgramsAnalysis directory and execute:-
python PositiveNGrams.py


For generation of Negative Ngrams, go to NgramsAnalysis directory and execute:-
python NegativeNGrams.py


Note:- If you want to generate both simultaneously, make two separate clones of the repository.


Copy the resulting phraseDictionary file from results directory to evaluate directory.
Important:- Call positive Ngrams file as positiveNgrams and negative Ngrams file as negativeNgrams.

Run filterOutCommon.py to keep Ngrams which only appear in positiveNgrams or negativeNgrams.
Results will be available in positiveNgramsFiltered and negativeNgramsFiltered.

Run positiveAndNegativeNgrams.py to calculate accuracy or find occurrences of each Ngram.
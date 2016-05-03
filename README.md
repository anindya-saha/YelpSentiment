# YelpSentiment
CSCE-689 NLP Seminar Course Project - Yelp Reviews Sentiment Analysis

Sentiment analysis (also known as opinion mining) refers to the use of natural language processing, text analysis and computational linguistics to identify and extract subjective information in source materials. Sentiment analysis is widely applied to reviews and social media for a variety of applications, ranging from marketing to customer service.

Sentiments or opinions can be expressed on different entities, such as a cell phone, a digital camera, or a bank. Sentiments can also be expressed on features or aspects of entities e.g. the screen of a cell phone, the service of a restaurant, or the picture quality of a camera.

The dataset for this project was chosen from the RecSys Challenge 2013: Yelp business rating prediction hosted by Kaggle in 2013 https://www.kaggle.com/c/yelp-recsys-2013/data. The dataset is yelp_restaurants_reviews.csv file located in the data folder.

There are two parts to this project. In the 1st part we learn more about NLP techniques and understand how can NLP techniques be leveraged to generate better features that can be subsequently used in the subsequent Machine Learning rounds. In the 2nd part we generate N-gram positive and negative lexicon incrementally from a group of seed words through an unsupervised learning process.

First Part
==========
yelp-reviews-sentiment.ipynb was done before mid-term and yelp-reviews-sentiment-6.ipynb and yelp-reviews-sentiment-7.ipynb was done for the final term. All the codes are written in the form of IPython notebooks and are self-explanatory. The codes, graphs and results all reside on the same notebook and can be reproduced following the codes as is done on the notebooks. The IPython notebook and data folder needs to be downloaded in the local machine to execute the IPython notebook codes.

For more details on how to execute IPython notebooks please refer to http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html

Second Part
===========
Generating Ngrams:

- For generation of Positive Ngrams, go to NgramsAnalysis directory and execute:-
python PositiveNGrams.py

- For generation of Negative Ngrams, go to NgramsAnalysis directory and execute:-
python NegativeNGrams.py

Note:- If you want to generate both simultaneously, make two separate clones of the repository.

- Copy the resulting phraseDictionary file from results directory to evaluate directory.
Important:- Call positive Ngrams file as positiveNgrams and negative Ngrams file as negativeNgrams.

- Run filterOutCommon.py to keep Ngrams which only appear in positiveNgrams or negativeNgrams.
Results will be available in positiveNgramsFiltered and negativeNgramsFiltered.

- Run positiveAndNegativeNgrams.py to calculate accuracy or find occurrences of each Ngram.

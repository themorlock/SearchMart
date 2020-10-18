import gensim
from sklearn import svm
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump, load
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

import sys

def k_means_sort(e):
	global product_terms, query
	occurences = 0
	for word in [x.lower() for x in e.split(',')[1].split('-')]:
		if word in product_terms or word in query.split(' '):
			occurences += 1
	occurences /= len(e.split(',')[1].split('-'))
	average_similarity = 0
	counter = 0
	for word in [x.lower() for x in e.split(',')[1].split('-')]:
		for query_word in query.split(' '):
			if query_word in word2vec_model.wv.vocab and word in word2vec_model.wv.vocab:
				aevrage_similarity += word2vec_model.similarity(query_word, word)
				counter += 1
	average_similarity /= (counter if counter != 0 else 1)
	return occurences + average_similarity

word2vec_model = gensim.models.Word2Vec.load('../MachineLearningModels/Word2Vec/word2vec.model')

vectorizing_model = load('../MachineLearningModels/KMeansClustering/vectorizing_model.sav')
clustering_model = load('../MachineLearningModels/KMeansClustering/clustering_model.sav')
products = open('../formatted_data/all_products.txt').read().split('\n')[:-1]

query = sys.argv[1]
prediction = clustering_model.predict(vectorizing_model.transform([query]))[0]
product_terms = [vectorizing_model.get_feature_names()[product_term_index] for product_term_index in clustering_model.cluster_centers_.argsort()[:, ::-1][prediction, :30]]
stop_words = set(stopwords.words('english')) 
product_terms = [w for w in product_terms if not w in stop_words] 

relavant_products = products.copy()
relavant_products.sort(key=k_means_sort, reverse=True)

print(relavant_products[:10])
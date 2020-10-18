import gensim
from sklearn import svm
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump, load
import flask
from flask_restful import Resource, Api, reqparse
from flask import request
from functools import partial
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def k_means_sort(e, product_terms, query):
	#global product_terms, query
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
				average_similarity += word2vec_model.similarity(query_word, word)
				counter += 1
	average_similarity /= (counter if counter != 0 else 1)
	return occurences + average_similarity

word2vec_model = gensim.models.Word2Vec.load('../MachineLearningModels/Word2Vec/word2vec.model')
vectorizing_model = load('../MachineLearningModels/KMeansClustering/vectorizing_model.sav')
clustering_model = load('../MachineLearningModels/KMeansClustering/clustering_model.sav')
products = open('../formatted_data/all_products.txt').read().split('\n')[:-1]

@app.route('/', methods=['GET'])
def home():
	parser = request.args
	#parser.add_argument('query', type=str)
	query = parser['query']
	prediction = clustering_model.predict(vectorizing_model.transform([query]))[0]
	product_terms = [vectorizing_model.get_feature_names()[product_term_index] for product_term_index in clustering_model.cluster_centers_.argsort()[:, ::-1][prediction, :30]]
	relavant_products = products.copy()
	relavant_products.sort(key=partial(k_means_sort, product_terms=product_terms, query=query), reverse=True)
	return jsonify(relavant_products[:10])
	#return "Distant Reading Archive: This site is a prototype API for distant reading of science fiction novels."

app.run()
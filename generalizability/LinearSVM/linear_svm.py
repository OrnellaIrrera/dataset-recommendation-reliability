
"""
In this module the classifiers SVM, Random Forest, Logistic Regression, Gaussian Naive Bayes,
Multinomial Naive Bayes, Complement Naive Bayes, CNN, LSTM, Simple RNN, CNN-LSTM and
Bidirectional LSTM are trained on the tfidf text representations of training data. Hyperparmeter
optimization of all models except Gaussian Naive Bayes is applied and the models are evaluated.
"""

import sys
import argparse

# comment if needed
sys.path.append('/path/to/your/folder/if/you/run/on/server/')
sys.path.append('../..')
##
from sklearn import decomposition
import re
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

import pickle
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, MultiLabelBinarizer
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB
from sklearn.multiclass import OneVsRestClassifier
from keras import datasets, layers, models, losses
from keras.activations import relu, elu
import numpy as np
# import talos
import sys
import time
import json
from helpers import preprocessing
from helpers import evaluation
import os
import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import random




def preprocess_string(input_string):
    # Remove newline characters, tab characters, and spaces
    cleaned_string = re.sub(r'[\n\t\s]', ' ', input_string)
    
    # Remove special characters and punctuation
    cleaned_string = re.sub(r'[^A-Za-z0-9 ]', '', cleaned_string)
    
    # Remove extra spaces and convert to lowercase
    cleaned_string = ' '.join(cleaned_string.split()).lower()
    
    return cleaned_string

#open sample data for abstracts or citations, for citations encoding 'ISO-8859-1' needs to be specified
dataframe = open('path/to/Abstract_New_Database.txt')



documentation_file_parameteropt = open("path/to/results/mes/parameter_optimization_tfidf_finale1.txt", "w+")
documentation_file_modelopt = open(".path/to/results/mes/classifier_optimization_tfidf_finale1.txt", "w+")

titles = []
with open(".path/to/data/mes/Dataset_Titles.txt") as titles_file:
    for line in titles_file:
        titles.append(line.replace("\n", ""))

#create list with preprocessed text and corresponding datasets for traditionale machine learning
preprocessed_data_list = []
preprocessed_data_list_single = []

i = 0

# this file contains the data processing in order to do avoid do the processing all the times the code is run.
if os.path.exists('path/to/data/tmp/mes/aux_store_data.json'):
    f = open('path/to/data/tmp/mes/aux_store_data.json','r')
    data = json.load(f)
    datasets = data['datasets']
    queries = data['queries']
    datasets_single = data['datasets_single']
    queries_single = data['queries_single']
    query_ids = data['queries_id']


    print(len(datasets))
    print(len(queries))
    print(len(datasets_single))
    print(len(queries_single))
    print(len(query_ids))

else:
    for i, line in enumerate(dataframe):
        if i % 100 == 0:
            print(i)
        id = str(line).split("\t")[0]
        query = str(line).split("\t")[1].replace("\n", "").strip()
        for title in titles:
            title_fil = preprocess_string(title)
            query_fil = preprocess_string(query)
            query = query_fil.replace(title_fil, "")
        dataset = str(str(line).split("\t")[2]).replace("\n", "").strip()
        final_dataset = dataset.split(", ")
        preprocessed_query = preprocessing_original.preprocess(query)
        preprocessed_tuple = (final_dataset, preprocessed_query,id)
        preprocessed_tuple_single = (dataset, preprocessed_query,id)
        preprocessed_data_list.append(preprocessed_tuple)
        preprocessed_data_list_single.append(preprocessed_tuple_single)
        i += 1
    datasets, queries,query_ids = zip(*preprocessed_data_list)
    datasets_single, queries_single,query_ids_single = zip(*preprocessed_data_list_single)
    g = open('path/to/data/tmp/mes/aux_store_data.json','w')
    json.dump({'queries_id':query_ids,'datasets':datasets,'datasets_single':datasets_single,'queries':queries,'queries_single':queries_single},g)

q_tfidf = preprocessing_original.tfidf(queries)
documentation_file_parameteropt.write("tfidf Evaluation \n")
documentation_file_modelopt.write("tfidf Evaluation \n")
print("  Actual number of tfidf features: %d" % q_tfidf.get_shape()[1])


d_train, d_test, q_train_ids, q_test_ids = train_test_split(datasets, query_ids, test_size=0.2)
q_train_indexes = [query_ids.index(q) for q in q_train_ids]
q_test_indexes = [query_ids.index(q) for q in q_test_ids]


json_data = {}
json_data['training'] = {}
json_data['test'] = {}
json_data['training']['queries'] = [queries[q] for q in q_train_indexes]
json_data['training']['query_ids'] = q_train_ids
json_data['training']['datasets'] = d_train
json_data['test']['queries'] = [queries[q] for q in q_test_indexes]
json_data['test']['query_ids'] = q_test_ids
json_data['test']['datasets'] = d_test
print(q_tfidf.shape)

# save split beacusa we will keep the training and test sets in all the experiments
if not os.path.exists('path/to/data/tmp/mes/split_train_test.json'):
    f = open('path/to/data/tmp/mes/split_train_test.json','w')
    json.dump(json_data,f)
    f.close()

q_train = q_tfidf[q_train_indexes]  # Contains the selected rows
q_test = q_tfidf[q_test_indexes]  # Contains all other rows

label_encoder = MultiLabelBinarizer()
label_encoder.fit(datasets)
d_train_encoded = label_encoder.transform(d_train)
pickle.dump(label_encoder, open('label_encoder_tfidf.sav', 'wb'))

start = time.time()
#Linear SVM: optimizing parameters with grid search
print("SVM model evaluation")
svm_dict = dict(estimator__C=[5,10,15,20,50,100])
classifier_svm = RandomizedSearchCV(estimator=OneVsRestClassifier(LinearSVC()),
                                    param_distributions=svm_dict,
                                    n_iter=5, n_jobs=-1)
classifier_svm.fit(q_train, d_train_encoded)
documentation_file_parameteropt.write(
    "Linear SVM: Best parameters {}, reached score: {} \n".format(
        classifier_svm.best_params_, classifier_svm.best_score_))
svm_model = classifier_svm.best_estimator_
pickle.dump(svm_model, open("svm_tfidf.sav", 'wb'))
pred_svm = svm_model.predict(q_test)
svm_evaluation_scores, svm_cm = evaluation_original.multilabel_evaluation_multilabelbinarizer(
    d_test, label_encoder.inverse_transform(pred_svm), "LinearSVM")
documentation_file_modelopt.write(svm_evaluation_scores)
documentation_file_parameteropt.close()
documentation_file_modelopt.close()
end = time.time()
print('finished in ',end-start)

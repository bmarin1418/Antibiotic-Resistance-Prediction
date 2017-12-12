import numpy as np
import pandas as pd
import os
import collections
import random
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# Get the feature space dimension so we can initialize the data matrix
kmer_cnts = collections.defaultdict(lambda:0)
genome_files = [file_nm for file_nm in os.listdir('./pen_cnts')]
for file_nm in genome_files:
    with open('./pen_cnts/' + file_nm, 'r') as fd:
        kmer_ids = set(fd.readlines()[0].rstrip().split(' '))
        for k_id in kmer_ids:
            kmer_cnts[k_id] += 1

print('The number of kmers is {}'.format(len(kmer_cnts)))

num_map = {}
num = 0
for k_id in kmer_cnts:
    num_map[k_id] = num

def createMatrix(mat, genome_files):
    for row_i, file_nm in enumerate(genome_files):
        with open('./pen_cnts/' + file_nm, 'r') as fd:
                 kmer_ids = set(fd.readlines()[0].rstrip().split(' '))
                 for k_id in kmer_ids:
                    mat[row_i, num_map[k_id]] = 1
    return mat

def createLabels(labels, genome_files):    
    for row_i, file_nm in enumerate(genome_files):
        genome_id = file_nm.partition('.PATRIC')[0]
        pheno = truth_dat[truth_dat['genome_id'] == genome_id].iloc[0]['resistant_phenotype']
        if pheno == 'Susceptible' or pheno == 'Intermediate':
             labels[row_i, 0] = 1
    return labels

train_matrix = np.zeros([100, len(kmer_cnts)], dtype=np.int8)
test_matrix = np.zeros([50, len(kmer_cnts)], dtype=np.int8) 
print('matrices malloced')
train_labels = np.zeros([100,1])
test_labels = np.zeros([50, 1])

random.shuffle(genome_files)
train_files = genome_files[:100]
test_files = genome_files[100:150]

truth_dat = pd.read_csv("PATRIC_genomes_AMR.tsv", sep='\t', dtype=str)
truth_dat = truth_dat[truth_dat['antibiotic'] == 'penicillin']

train_matrix = createMatrix(train_matrix, train_files)
test_matrix = createMatrix(test_matrix, test_files)
train_labels = createLabels(train_labels, train_files)
test_labels = createLabels(test_labels, test_files)


clf = RandomForestClassifier(n_jobs=36, max_features="sqrt", n_estimators=50)
print('training started')
clf.fit(train_matrix, np.ravel(train_labels))
preds = clf.predict(test_matrix)
print('training finished')
np.save('preds', preds)
np.save('labels', np.ravel(test_labels))

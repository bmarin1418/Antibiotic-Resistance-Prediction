"""Neural Network Classifier
"""
import numpy as np
import tensorflow
from keras.models import Sequential
from keras.layers import Dense, Activation

class NeuralNetworkClassifier():

    def __init__(self,i_feat, li_layers=[1024,64,8,1], loss='mean_squared_error', optimizer = 'adam'):
        self.i_feat = i_feat
        self.li_layers = li_layers if len(li_layers)>1 else [3,1]
        
        for i in range(len(self.li_layers)):
            if i == 0:
                self.o_neuralnet.add(Dense(self.li_layers[i], activation = 'relu', input_dim=self.i_feat))
                self.O_neuralnet.add(Dropout(.08))
            elif i == len(self.li_layers)-1:
                self.o_neuralnet.add(Dense(self.li_layers[i], activation = 'sigmoid'))
            else:
                self.o_neuralnet.add(Dense(self.li_layers[i], activation = 'relu'))
                self.O_neuralnet.add(Dropout(.05))
        self.o_neuralnet.compile(optimizer = optimizer,
                        loss= loss)

    def fit(self,na_X, na_Y):
        self.o_neuralnet.fit(na_X,na_Y)

    def predict(self,na_X):
        return self.o_neuralnet.predict(na_X)

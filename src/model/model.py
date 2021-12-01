import pickle
import os
import pandas as pd
from src.query import Query
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.tree import export_text

class ModelGenerator(object):
  
  def __init__(self):
    self._data = pd.read_csv('data/heart_failure_dataset.csv')
    self._modelos = 'models/'
    self._model = RandomForestClassifier(n_estimators = 50)

  def createModel(self):
    X_train, X_test, y_train, y_test = train_test_split(
        self._data.drop(['death'], axis ='columns'),
        self._data['death'],test_size=0.2)

    self._model.fit(X_train, y_train)

  def loadModel(self, fileName):
    if os.path.isfile(self._modelos + fileName + '.sav'):
      with open(self._modelos + fileName + '.sav', 'rb') as f:
        self._model = pickle.load(f)
    else:
      raise Exception()

  def saveModel(self, fileName):
    with open(self._modelos + fileName + '.sav', 'wb') as f:
      pickle.dump(self._model, f)

  def useModel(self, query):
    answer = self._model.predict(query)

    if answer[0] == 0:
      result = 'vivirá'
    elif answer[0] == 1:
      result = 'morirá'
    else:
      raise Exception('Error al usar el modelo')

    return result

  def modelScore(self, testSize):
    X_train, X_test, y_train, y_test = train_test_split(
        self._data.drop(['death'], axis ='columns'),
        self._data['death'],test_size=testSize)
    
    return self._model.score(X_test, y_test)

  def createGraph(self):
    f_names = []
    for col in self._data.columns:
        if col != 'death':
            f_names.append(col)
    
    estimator = self._model.estimators_[5]

    text_representation = export_text(estimator)
    return text_representation

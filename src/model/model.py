import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class ModelGenerator(object):
  
  def __init_(self):
    self.datos = 'datos/heart_failure_dataset.csv'

  def createModel(self):
    data = pd.read_csv(self.datos)

    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(['death'], axis ='columns'),
        data['death'],test_size=0.2)

    model = RandomForestClassifier(n_estimators = 50)
    model.fit(X_train, y_train)

    return model


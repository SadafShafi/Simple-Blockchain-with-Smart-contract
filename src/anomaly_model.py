import numpy as np
import pandas as pd

from sklearn.ensemble import IsolationForest

import pickle

data = pd.read_csv('temp_data.csv')

model = IsolationForest(n_estimators=100, max_samples='auto',random_state=0).fit(data[['temp']].to_numpy())

data['scores'] = model.decision_function(data[['temp']].to_numpy())
data['anomaly_score'] = model.predict(data[['temp']].to_numpy())

pickle.dump(model, open('anomaly_detector.sav', 'wb'))

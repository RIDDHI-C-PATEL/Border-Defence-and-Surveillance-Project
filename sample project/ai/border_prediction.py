import numpy as np
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

X = [[1,1],[2,2],[3,3]]
y = [0,1,1]

model.fit(X,y)

def predict(zone):
    return model.predict([zone])
import numpy as np
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

X = [[1,2],[2,3],[3,4]]
y = [0,1,0]

model.fit(X,y)

def predict(data):
    return model.predict([data])
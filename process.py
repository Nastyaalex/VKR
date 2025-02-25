import pickle
import sklearn
import numpy as np

def get_prediction(area1,area2,area3,area4,area5,area6,area7,area8,area9,area10,area11,area12):
    with open('lr_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    data = [area8,area1,area2,area3,area4,area5,area6,area7,area9,area10,area11,area12]

    y_pred = loaded_model.predict(np.array(data).reshape(1, -1).astype(float))
    return y_pred
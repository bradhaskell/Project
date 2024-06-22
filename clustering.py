from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd 

def train_clustering_model():
    data = pd.read_csv('data/users.csv', header=None)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(scaled_data)
    return kmeans
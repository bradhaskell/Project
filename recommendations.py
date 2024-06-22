from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pandas as pd

def train_recommendation_model():
    ratings_dict = {
        'user_id': [1, 1, 1, 2, 2, 3, 3, 4],
        'workout_id': [1, 2, 3, 1, 2, 2, 3, 3],
        'rating': [5, 4, 3, 5, 4, 2, 4, 5]
    }
    df = pd.DataFrame(ratings_dict)
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'workout_id', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.25)
    algo = SVD()
    algo.fit(trainset)
    return algo

class RecommendationModel:
    def __init__(self, model):
        self.model = model

    def recommend(self, user_id):
        # Generate workout recommendations for the user
        return "Sample Workout Plan"

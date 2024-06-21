from flask import Flask, request, jsonify
from models.clustering import train_clustering_model
from models.recommendation import train_recommendation_model
import pandas as pd

app = Flask(__name__)

clustering_model = train_clustering_model()
recommendation_model = train_recommendation_model()

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    df = pd.DataFrame([user_data])
    df.to_csv('data/users.csv', mode='a', header=False, index=False)
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/workout-plan/<int:user_id>', methods=['GET'])
def get_workout_plan(user_id):
    user_cluster = clustering_model.predict([[user_id]])[0]
    workout_plan = recommendation_model.recommend(user_id)
    return jsonify({"user_id": user_id, "plan": workout_plan})

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    feedback = request.json
    # Process feedback
    return jsonify({"message": "Feedback received!"})

if __name__ == '__main__':
    app.run(debug=True)

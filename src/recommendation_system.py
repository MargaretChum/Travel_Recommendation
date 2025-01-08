from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# Sample destination data for recommendation
def destination_data():
    data = {
        'destination': ['Switzerland', 'Bangkok', 'Japan', 'New Zealand'],
        'activity': ['Skiing', 'Street Food', 'Hiking', 'Hiking'],
        'environment': ['Snowy Mountains', 'Bustling Streets', 'Mountain Views', 'Mountain Views']
    }
    return pd.DataFrame(data)

# Simple function to get recommendations
def recommend(user_activity, user_environment):
    destinations = destination_data()
    
    # Convert activities and environments into a simple vector (this is just a placeholder)
    activity_vec = np.array([1 if activity == user_activity else 0 for activity in destinations['activity']])
    env_vec = np.array([1 if environment == user_environment else 0 for environment in destinations['environment']])

    user_vector = activity_vec + env_vec

    # Calculate cosine similarity
    similarities = []
    for index, row in destinations.iterrows():
        destination_vector = np.array([1 if activity == row['activity'] else 0 for activity in destinations['activity']])
        destination_vector += np.array([1 if environment == row['environment'] else 0 for environment in destinations['environment']])
        similarity = cosine_similarity([user_vector], [destination_vector])
        similarities.append(similarity[0][0])

    # Add similarity to destination data and return recommendations
    destinations['similarity'] = similarities
    return destinations.sort_values('similarity', ascending=False)[['destination', 'similarity']]

# Test function
if __name__ == "__main__":
    recommended = recommend('Hiking', 'Mountain Views')
    print(recommended)

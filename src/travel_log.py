import pandas as pd

# Create a sample travel log
def create_travel_log():
    data = {
        'user_id': [1, 2, 3],
        'destination': ['Switzerland', 'Bangkok', 'Japan'],
        'activity': ['Skiing', 'Street Food', 'Hiking'],
        'environment': ['Snowy Mountains', 'Bustling Streets', 'Mountain Views'],
        'rating': [5, 4, 5],
        'notes': ['Loved the views', 'Amazing food', 'Great hiking trails']
    }
    df = pd.DataFrame(data)
    return df

# Test function
if __name__ == "__main__":
    log = create_travel_log()
    print(log)

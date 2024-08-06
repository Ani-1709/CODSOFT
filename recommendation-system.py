import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: User ratings for different movies
data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'movie_id': [101, 102, 103, 101, 104, 105, 102, 104, 106],
    'rating': [5, 3, 4, 4, 5, 2, 4, 4, 5]
}

# Sample data: Movie names mapping
movie_names = {
    101: "Movie A",
    102: "Movie B",
    103: "Movie C",
    104: "Movie D",
    105: "Movie E",
    106: "Movie F"
}

# Create a DataFrame
ratings_df = pd.DataFrame(data)

# Create a pivot table with users as rows and movies as columns
user_movie_matrix = ratings_df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix)

# Convert the similarity matrix to a DataFrame for easier handling
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# Function to get movie recommendations for a user
def get_movie_recommendations(user_id, user_movie_matrix, user_similarity_df, movie_names, num_recommendations=3):
    # Get the movies rated by the user
    user_ratings = user_movie_matrix.loc[user_id]
    
    # Get similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    
    # Aggregate ratings from similar users
    similar_user_ratings = user_movie_matrix.loc[similar_users]
    
    # Calculate weighted average ratings for each movie
    weighted_ratings = similar_user_ratings.T.dot(user_similarity_df[user_id].sort_values(ascending=False)[1:])
    
    # Normalize by the sum of similarities
    weighted_ratings /= user_similarity_df[user_id].sort_values(ascending=False)[1:].sum()
    
    # Get movies the user hasn't rated yet
    unrated_movies = user_ratings[user_ratings == 0].index
    
    # Filter for unrated movies
    recommendations = weighted_ratings[unrated_movies].sort_values(ascending=False).head(num_recommendations)
    
    # Convert movie IDs to movie names
    recommendations.index = recommendations.index.map(movie_names)
    
    # Convert the recommendations to a more readable format
    recommendations_df = pd.DataFrame(recommendations, columns=['predicted_rating'])
    recommendations_df.index.name = 'movie_name'
    
    return recommendations_df

# Example usage: Get recommendations for user 1
user_id = 1
recommendations = get_movie_recommendations(user_id, user_movie_matrix, user_similarity_df, movie_names)
print(f"Recommended movies for user {user_id}:")
print(recommendations)

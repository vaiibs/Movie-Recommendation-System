import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process
import streamlit as st

# Load the dataset
data = pd.read_csv('movies.csv')

# Fill NaN values with empty strings in the relevant columns
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
data[selected_features] = data[selected_features].fillna('')

# Combining relevant features into a single string
combined_features = data['genres'] + ' ' + data['keywords'] + ' ' + data['tagline'] + ' ' + data['cast'] + ' ' + data['director']

# Converting the text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)

# Create a list of all movie titles
list_of_all_titles = data['title'].tolist()

# Streamlit App
st.title("Movie Recommendation System")
st.header("Get Recommendations Based on Your Favorite Movie")

# User input
movie_name = st.text_input("Enter your favorite movie name:")

if st.button("Get Recommendations"):
    if movie_name:
        # Use fuzzy matching to find the best match
        best_match = process.extractOne(movie_name, list_of_all_titles)

        if best_match and best_match[1] > 70:  # Set a threshold for similarity
            close_match = best_match[0]
            index_of_the_movie = data[data.title == close_match]['index'].values[0]

            # Getting similarity scores for the matched movie
            similarity_score = list(enumerate(similarity[index_of_the_movie]))

            # Sorting similar movies based on their similarity score
            sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

            # Display recommended movies
            st.subheader(f"Movies suggested for you based on '{close_match}':")
            for i, movie in enumerate(sorted_similar_movies):
                if i < 10:  # Limit to top 10 movies
                    index = movie[0]
                    title_from_index = data[data.index == index]['title'].values[0]
                    st.write(f"{i + 1}. {title_from_index}")
        else:
            st.warning("Sorry, no similar movies found. Please try with a different name.")
    else:
        st.warning("Please enter a movie name.")

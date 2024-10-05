# Movie Recommendation System

Objective:

To create a movie recommendation system that suggests movies based on a user's input.


Steps Involved

    Data Collection:
      Gather a dataset (movies.csv) containing movie information (genres, keywords, tagline, cast, director, title).
    
    Data Preparation:
      Load and clean the dataset using pandas.
    
    Feature Selection: 
      Choose relevant features for recommendations.
    
    Data Processing:
      Combine selected features into a single string for each movie.
      Use TfidfVectorizer to convert text data into numerical feature vectors.
      
    Calculating Similarity:
        Compute cosine similarity between the feature vectors.
    
    User Interaction:
      Prompt the user for their favorite movie title.
      Use fuzzywuzzy to find the closest match from the movie titles.
      
    Recommendation Generation:
      If a close match is found, retrieve its index and calculate similarity scores against other movies.
      Sort and suggest the top N similar movies.
      
    Output: 
      Present the recommended movies to the user.

Technologies Used:

    Programming Language: Python
    Libraries:
    Pandas: Data manipulation
    NumPy: Numerical operations
    Scikit-learn: Machine learning tools (TfidfVectorizer, cosine similarity)
    FuzzyWuzzy: String matching for user input
    
    
![image](https://github.com/user-attachments/assets/fba095a8-ec1e-4d83-b4ab-688253519d10)

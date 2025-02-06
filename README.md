# Movie Recommender System - TMDB Dataset

This project implements a **Content-Based Movie Recommender System** using the TMDB (The Movie Database) dataset. The system uses **Cosine Similarity** to recommend movies based on their features such as genres, keywords, cast, crew, and the movie overview.

https://nextflick-movie-recommender.streamlit.app/ 

## Project Overview

The movie recommender system is built using the following steps:

1. **Data Preprocessing:**
   - Merging `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` datasets.
   - Extracting key features like `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.
   - Cleaning and processing text data to create a consolidated 'tags' column.

2. **Feature Engineering:**
   - Combining movie-related features into a single text column.
   - Vectorizing the combined text using CountVectorizer.

3. **Cosine Similarity:**
   - Calculating cosine similarity scores between movies to measure content similarity.

4. **Recommendation Function:**
   - Implementing a function to recommend top 5 movies based on similarity scores.

5. **Model Serialization:**
   - Saving the similarity matrix and movie data using Pickle for easy deployment.

---

## Web Application with Streamlit

To enhance the user experience, the movie recommender system is deployed as an interactive web application using **Streamlit**.

### Key Features
- **Movie Selection Dropdown:** Users can choose any movie from the dropdown list.
- **Personalized Recommendations:** Displays the top 5 recommended movies based on the selected title.
- **Poster Integration:** Movie posters are fetched dynamically using the TMDB API.

### API Configuration

- Replace `YOUR_API_KEY` in the script with your TMDB API key to fetch movie posters.

### Conclusion

This interactive web application enhances the recommender system with an intuitive UI and visual recommendations. It demonstrates the integration of machine learning models into real-world applications.



import os
import streamlit as st
import pickle
import pandas as pd
import requests # to hit API
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def download_s3_file(url, local_filename):
    if os.path.exists(local_filename):
        print(f"{local_filename} already exists. Skipping download.")
        return
    try:
        with requests.get(url, stream=True, timeout=300) as response:
            response.raise_for_status()
            with open(local_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            print(f"{local_filename} downloaded successfully to the root directory!")
    except requests.exceptions.Timeout:
        print(f"The request for {local_filename} timed out. Try increasing the timeout value.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_poster(movie_id):
    api_key = os.getenv('TMDB_API_KEY')
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters
    
download_s3_file("https://flixly-movie-recommendation.s3.us-east-2.amazonaws.com/movieDict.pkl", "movieDict.pkl")
download_s3_file("https://flixly-movie-recommendation.s3.us-east-2.amazonaws.com/similarity.pkl", "similarity.pkl")

movie_dict = pickle.load(open('movieDict.pkl','rb'))
movies =pd.DataFrame(movie_dict)  
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Show me something that’s worth the popcorn',
     (movies['title']).values)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
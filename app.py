import pickle
import streamlit as st
import requests

#https://drive.google.com/file/d/17NRVIJ6L0XCWto99e7hpP5Qn2EVuiILp/view?usp=sharing

import gdown

# Replace with your Google Drive file ID
file_id = '17NRVIJ6L0XCWto99e7hpP5Qn2EVuiILp'
url = f'https://drive.google.com/uc?id={file_id}'

# Download the file
gdown.download(url, 'similarity.pkl', quiet=False)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
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


st.header('Movie Recommender System')
movies = pickle.load(open('movies_list.pkl','rb'))
#similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Display recommendations in a single row
    cols = st.columns(5)  # Create 5 columns for the 5 recommendations

    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])  # Show movie name
            st.image(recommended_movie_posters[i],use_container_width=True)  # Show movie poster'''


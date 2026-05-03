import pickle
import streamlit as st
import requests
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    return [movies.iloc[i[0]].title for i in movies_list[1:6]]

    recommended_movie = []
    for i in movies_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie
movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie from the dropdown',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write('Recommended Movies:')
    for i in recommendations:
        st.write(i)
        



import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{0}?api_key=28540fedfe0c45b3f06872e01f69601f&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommended system")


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    recommended_movie=[]
    recommended_movie_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id

        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))

    return recommended_movie,recommended_movie_poster

selected_movies_name = st.selectbox(
'Select a Movie',
movies['title'].values
)


if st.button('Recommend'):
    names,poster=recommend(selected_movies_name)
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.header(names[0])
        st.image(poster[0])
    with col2:
        st.header(names[1])
        st.image(poster[1])
    with col3:
        st.header(names[2])
        st.image(poster[2])
    with col4:
        st.header(names[3])
        st.image(poster[3])
    with col5:
        st.header(names[4])
        st.image(poster[4])






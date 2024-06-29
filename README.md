## Movie Recommender system

### Objective:
The primary objective of the movie recommender system project is to develop a machine learning nad NLP model which is capable of suggesting popular movies based on popularity, content based recommendation and collaborative filtering. The classifier is trained on a dataset fetched from TMDB contains movie_id, title, overview, cast, crew, vote_average, vote_count etc.

### Technical skill:

1. Python
2. pandas
3. Machine learning algorithms
4. NLP
5. Streamlit
6. Data manipulation

### Workflow Overview:
1. Data collection: Collected the data from TMDB api using request library by web scraping.
2. Data pre-process: As the raw data cant be directly used for model because of poor data quality. I preprocessed the raw data to enhance the quality of data which increases the reliability on the model, accuracy of the prediction, consistenancy and decision making ability.
   - Dealing with Duplicate rows and Null values.
   - Case normalization.
   - Text cleaning.
   - Tokenization.
   - Stemming
   - graphical visualization to deal with outliers and irrelevent movies.    
3. EDA: performed Exploratory data analysis to observe the data and find the insights and take action to build effective model.
4. Model Training:
   -At first built a recommender which will recommend movies based on the popularity, vote count and rating of the movies. i have created a weighted rating column based on IMDB rating   
    formula: (c*r/(c+C) + C*MR/(c+C))
        where C: minimum num of vote required to qualify the movie, MR : mean rating, r : rating of the movie, c: count of votes of the movie
   -Secondly improved the model by adding genre features. so if user want to get top movies based on particular genre then our recommeder system will be able to recommend.
   - BUild a content based recommender system which will take a movie name from user and evaluate the closet top 5 movies based  on the content of given movie. here i have created a 
     feature "tags" and it is the concatenation of genre, overview, keywords, cast and crew. it help us to get similar movies.
     First of all created input data by using text vectorization(TFIDF). then feed the data into cosine_similarity which helps to identify the nearest vectors(movies)
8. Model API: Created a web page so that any user can access and play with the product.



![Uber_analysis_dashboard](https://github.com/rockraj999/MovieRecommenderSystem/blob/main/Screenshot%20(83).png)


![Uber_analysis_dashboard](https://github.com/rockraj999/MovieRecommenderSystem/blob/main/Screenshot%20(84).png)


![Uber_analysis_dashboard](https://github.com/rockraj999/MovieRecommenderSystem/blob/main/Screenshot%20(85).png)


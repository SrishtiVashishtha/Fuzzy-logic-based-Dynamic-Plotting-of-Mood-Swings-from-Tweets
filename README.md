# Fuzzy-logic-based-Dynamic-Plotting-of-Mood-Swings-from-Tweets
This code performs the sentiment analysis of social media posts.


**Code for the paper**

[Fuzzy logic based Dynamic Plotting of Mood Swings from Tweets.](https://link.springer.com/chapter/10.1007/978-3-030-16681-6_13)

**Description**

This paper performs the sentiment analysis of social media posts particularly tweets.
The proposed approch uses linguistic hedges with fuzzy logic to compute the sentiment of tweet.
The tweets used in our experiments are extracted from the timeline of the India Vs Pakistan final ICC world-cup match in June 2017. They reflect the moods of the twitter users as the match progresses. Using our fuzzy logic based approach, we successfully plot the dynamic mood vs time and compute the polarity of the sentiment at each time instant.

**Dataset**

twittertweets.txt file contains the tweets used in our experiments.

**Running the model:**

tweets_Union file contains the code for implementing union operation on sentiment scores of tweets.

tweets_LH_FuzzyPos file contains the code for implementing lingustic hedge : 'More or less positive and not very negative' on sentiment scores of tweets.

tweets_LH_FuzzyNeg file contains the code for implementing lingustic hedge : 'More or less negative and not very positive' on sentiment scores of tweets.

tweets_SentimentResults file contains the code for computing the final sentiment of tweets.

FuzzyPos.pickle and FuzzyNeg.pickle files contain the output from tweets_LH_FuzzyPos and tweets_LH_FuzzyNeg files.


**Citation**

If using this code, please cite our work using :

>Vashishtha, Srishti, and Seba Susan. "Fuzzy Logic Based Dynamic Plotting of Mood Swings from Tweets." In International Conference on Innovations in Bio-Inspired Computing and Applications, pp. 129-139. Springer, Cham, 2018.

# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

access_token = "784881409521508352-gq69a9kmOLNUwqEBudGxg31j5hj79DA"
access_token_secret = "9LjMj0AflSe1LTJ5IPK5Qs56jQSZSuJKFeAXbh8QlMRar"
consumer_key = "8n7r008VE7xn1IdUWl0rmDMsk"
consumer_secret = "YGDQT0DB4e75wTg99GRo5oIv1SpYNThM99jRepDReJFAtMOENP"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

search_for_tweets = api.search('Hilary Clinton')
subjectivity = 0 
polarity = 0
count = 0
for tweet in search_for_tweets:
  print(tweet.text)
  count += 1
  analysis = TextBlob(tweet.text)
  subjectivity += analysis.sentiment.subjectivity 
  polarity += analysis.sentiment.polarity

print("\n")
print("The average subjectivity is " + str(subjectivity/count)) 
print("The average polarity is " + str(polarity/count))



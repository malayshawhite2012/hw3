# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "8n7r008VE7xn1IdUWl0rmDMsk",
    "consumer_secret"     : "YGDQT0DB4e75wTg99GRo5oIv1SpYNThM99jRepDReJFAtMOENP",
    "access_token"        : "784881409521508352-gq69a9kmOLNUwqEBudGxg31j5hj79DA",
    "access_token_secret" : "9LjMj0AflSe1LTJ5IPK5Qs56jQSZSuJKFeAXbh8QlMRar" 
    }

  api = get_api(cfg)
  tweet = "Hello, SI 206 CLASS! #UMSI-206 #Proj3"
  status = api.update_with_media("picofme.png", status=tweet) 


if __name__ == "__main__":
  main()
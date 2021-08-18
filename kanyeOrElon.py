import requests

req = requests.get(url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=100")
tweetData = r.json()
print(tweetData[0]['text'])

#GET https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=100

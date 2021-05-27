import os
import tweepy as tw
from django.conf import settings

def tweet_scrap(search_words):
    consumer_key = settings.TWITTER_API_KEY
    consumer_secret = settings.TWITTER_API_SECRET_KEY
    access_token = settings.TWITTER_ACCESS_TOKEN
    access_token_secret = settings.TWITTER_ACCESS_SECRET

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    tweets = tw.Cursor(api.search,
                       q=search_words,
                       include_entities=True).items(100)

    tweet_info_list = []
    id_cnt = 0
    for tweet in tweets:
        id_cnt += 1
        tweet_info = {}
        tweet_info["id"] = id_cnt
        tweet_info["text"] = tweet.text
        tweet_info["user_name"] = tweet.user.screen_name
        print(tweet.text, tweet.user.screen_name)
        if 'media' in tweet.entities:
            for image in tweet.entities['media']:
                tweet_info["image"] = tweet_info.get("image", [])
                tweet_info["image"].append(image['media_url'])
                print(image['media_url'])
                print(tweet_info["image"])
        tweet_info_list.append(tweet_info)
    return tweet_info_list


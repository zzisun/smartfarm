import os
import tweepy as tw
import pandas as pd
from django.conf import settings

def tweet_scrap():
    consumer_key = settings.TWITTER_API_KEY
    consumer_secret = settings.TWITTER_API_SECRET_KEY
    access_token = settings.TWITTER_ACCESS_TOKEN
    access_token_secret = settings.TWITTER_ACCESS_SECRET

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    search_words = ["#krishian_1_0_0"]
    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       include_entities=True).items(10)

    tweet_info_list = []
    for tweet in tweets:
        tweet_info = {}
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


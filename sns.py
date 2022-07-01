import snscrape.modules.twitter as sntwitter
import pandas as pd
import time
from random import randint

counter = 1
while counter < 5:
    if counter >= 10:
        start_date = f"2022-{counter}-01"
        end_date = f"2021-{counter}-28"
    else:
        start_date = f"2022-0{counter}-01"
        end_date = f"2022-0{counter}-28"

    maximum_tweets = 3000
    query = "startup tips"

    def cleaned_url(url):
        return str(url).replace("\\","")

    print(f"Starts scraping from {start_date} to {end_date}")
    # Creating list to append tweet data to
    tweet_data = []
    other_tweets = []
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} since:{start_date} until:{end_date} -filter:retweets -filter:links').get_items()):
        if i > maximum_tweets:
            break
        if tweet.lang == 'en':
            new_url = cleaned_url(tweet.url)
            if tweet.replyCount >= 3:
                tweet_data.append([tweet.date, tweet.id, tweet.renderedContent, tweet.user.username, tweet.replyCount, new_url, tweet.user.id])
            other_tweets.append([tweet.date, tweet.id, tweet.renderedContent, tweet.user.username, tweet.replyCount, new_url, tweet.user.id])
            
    print(f'{len(tweet_data) + len(other_tweets)} tweets scraped')
    print(f'{len(tweet_data)} is relevant')
    # Creating a dataframe from the tweets list above
    plotted_data = pd.DataFrame(tweet_data, columns=['date', 'id', 'body', 'username', 'reply_count', 'url','userid'])
    plotted_data.to_json(f'snsdata/{start_date}.json', orient='records')
    
    other_data = pd.DataFrame(other_tweets, columns=['date', 'id', 'body', 'username', 'reply_count', 'url','userid'])
    other_data.to_json(f'others/{start_date}.json', orient='records')
    
    print(f'{start_date}.json saved')
    counter = counter + 1
    #random number between 30 and 100 seconds
    sleep_time = randint(30, 100)
    print(f"Sleeping for {sleep_time}s")
    time.sleep(sleep_time)
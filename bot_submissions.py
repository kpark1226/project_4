import praw
import random
import time

reddit = praw.Reddit('bot', user_agent='cs40')

for i in range(400):
    list_of_subs = list(reddit.subreddit("liberal").hot(limit=None))
    submission = random.choice(list_of_subs)
    title = submission.title
    selftext = submission.selftext

    if selftext=='':
        url = submission.url
        subreddit = reddit.subreddit("cs40_2022fall")
        subreddit.submit(title, url=url)

    else:
        subreddit = reddit.subreddit("cs40_2022fall")
        subreddit.submit(title, selftext=selftext)
    print('Created a submission')

time.sleep(7)
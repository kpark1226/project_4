
import praw
from textblob import TextBlob 

reddit = praw.Reddit('bot', user_agent='cs40')


subreddit = reddit.subreddit('cs40_2022fall')

for submission in subreddit.top(limit=None):
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()

    not_my_comments = []

    for comment in all_comments:
        try:
            if comment.author=="bot40cs":
                pass
            else:
                not_my_comments.append(comment)
                if "Trump" in comment.body:
                    blob= TextBlob(comment.body)
                    if blob.semtiment.polarity>0:
                        comment.downvote()
                    else:
                        comment.upvote()        
        except AttributeError:
            print('not a comment')
    
            

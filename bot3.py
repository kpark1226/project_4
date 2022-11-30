import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "[OBAMA] was a [GREAT] [PRESIDENT].  He served as the 44th President of [AMERICA]. He is [TALL].",
    "I wish I had the [OPPORTUNITY] to vote for him. I [COULDN\'T] vote for him because I was under the age of 18. If he could run for President [AGAIN], I would [DEFINITELY] vote for [HIM].",
    "Obama [RESCUED] the [COUNTRY] from the Great Recession. He also signed the Affordable Care Act, which [PROVIDED] health insurance to over 20 million uninsured [AMERICANS]. On top of that, he [ENDED] the war in Iraq.",
    "Obama [PUSHED] federal agencies to become more eco-conscious. Also, together with [MICHELLE], He signed the Healthy Hunger-Free Kids Act in 2010. This [MANDATED] that $4.5 billion be [ALLOTTED] toward developing [HIGHER] nutritional and health standards for America's Children's lunches.",
    "[OBAMA] [BELIEVED] that the US [DERIVES] strength from the diversity of its [POPULATION] and from its commitment to equal opportunity for all. That is why they made diversity and inclusion a top priority inside the administration and [THROUGHOUT] the federal government.",
    "President Obama signed an Executive Order, [INCREASING] federal employment of [INDIVIDUALS] with disabilities. Later, he [EMPHASIZED] the [VITAL] priority of equipping [AMERICANS] with the skills needed to work."   
    ]

replacements = {
    'OBAMA' : ['Obama', 'Barack Obama', 'Michelle Obama\'s husband', 'Malia Obama\'s father'],
    'GREAT' : ['great', 'magnificent', 'fantastic', 'wonderful'],
    'PRESIDENT' : ['leader', 'figure', 'president'],
    'AMERICA' : ['America', 'the United States', 'the United States of America', 'the US'],
    'TALL'  : ['tall', '6\'2'],
    'OPPORTUNITY' : ['opportunity', 'chance', 'fun things'],
    'DEFINITELY' : ['definitely', 'surely', 'certainly'],
    'AGAIN' : ['again', 'once more', 'one more time'],
    'COULDN\'T' : ['couldn\'t', 'was not able to', 'could not'],
    'HIM' : ['him', 'Barack Obama', 'Obama'],
    'RESCUED' : ['rescued', 'saved', 'liberated'],
    'COUNTRY' : ['country', 'US', 'United States'],
    'PROVIDED' : ['provided', 'gave', 'supplied'],
    'ENDED' : ['ended', 'terminated', 'stopped'],
    'AMERICANS' : ['Americans', 'citizens', 'residents'],
    'PUSHED' : ['pushed', 'urged', 'impelled'],
    'MICHELLE' : ['Michelle Obama', 'his wife', 'Michelle', 'the first lady'],
    'MANDATED' : ['mandated', 'ordered', 'commanded'],
    'ALLOTTED' : ['allotted', 'assigned', 'issued', 'devoted'],
    'HIGHER' : ['higher', 'greater', 'better'],
    'BELIEVED' : ['believed', 'thought', 'felt'],
    'DERIVES' : ['derives', 'gets', 'obtains', 'acquires'],
    'POPULATION' : ['population', 'people', 'citizens', 'residents'],
    'THROUGHOUT' : ['throughout', 'all over', 'all around'],
    'INCREASING' : ['increasing', 'growing', 'improving', 'escalating'],
    'INDIVIDUALS' : ['individuals', 'those', 'people'],
    'EMPHASIZED' : ['emphasized', 'highlighted', 'stressed'],
    'VITAL' : ['vital', 'crucial', 'key']
    }

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot3', user_agent='cs40')

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://old.reddit.com/r/cs40_2022fall/comments/ywdc19/cs40_zogobot_test/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comment_sort = 'top'
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author != 'kpbot3':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        submission.reply(generate_comment())
        print('top level comment')

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            has_not_replied = True
            for reply in comment.replies:
                if reply.author == 'kpbot3':
                    has_not_replied = False
                    break
            if has_not_replied:
                comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        try:
            top_comment = comments_without_replies[0]
            top_comment.reply(generate_comment())
            print('replied to random comment')
        except IndexError:
            print('replied to all comments')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    list_of_subs = list(reddit.subreddit("cs40_2022fall").hot(limit=5))
    submission = random.choice(list_of_subs)
    



    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(4)
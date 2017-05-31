import random
import praw
import os
import re

def mockery(in_string):

    mocked = ''

    # Makes long runs less likely, maximum run is equal to pool size.
    max_run = 3
    rand_pool = [random.choice([True, False]) for _ in range(max_run)]
    for c in in_string:
        if c is not ' ':
            capitalize = random.choice(rand_pool)
            rand_pool.remove(capitalize)
            if capitalize:
                c = c.upper()
                rand_pool.append(False)
            else:
                c = c.lower()
                rand_pool.append(True)
        mocked += c

    return mocked

reddit = praw.Reddit('reeddit_bot')

subreddit = reddit.subreddit('pythonforengineers') #free for testing
#subreddit = reddit.subreddit('TumblrInAction')

for comment in subreddit.stream.comments():

    if not os.path.isfile("already_mocked.txt"):
        already_mocked = []
    else:
        with open("already_mocked.txt", "r") as log:
            already_mocked = log.read()
            already_mocked = already_mocked.split("\n")
            already_mocked = list(filter(None, already_mocked))

    if re.search("MoCkEd", comment.body):
        if comment.id not in already_mocked:
            post = comment.submission
            if not comment.is_root:
                parent = comment.parent()
                print("Replying to " + parent.id + " in post " + post.id)
                answer = mockery(parent.body)
                #print(answer)
                comment.reply(answer)
            elif comment.is_root:
                print("Replying to " + post.id)
                comment.reply(mockery(post.title))
            already_mocked.append(comment.id)
    if re.search("reeddit", comment.body, re.IGNORECASE):
        if comment.id not in already_mocked:
            post = comment.submission
            print("Was triggered by " + comment.id + " in post " + post.id + ". Am literally shaking")
            comment.reply("That was one of my trigger words!\nREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!")
            already_mocked.append(comment.id)
    with open("already_mocked.txt", "w") as f:
        for comment_id in already_mocked:
            f.write(comment_id + "\n")

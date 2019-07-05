import praw
import pdb
import re
import os
import random

reddit = praw.Reddit('bot1')
subR = input("Which subreddit? ")
subR = str(subR)
subreddit = reddit.subreddit(subR)


for submission in subreddit.hot(limit=5):
    print("Title: ",submission.title)
    print("Author: ",submission.author)
    print("Upvotes: ",submission.ups)
    print("Downvotes: ",submission.downs)


if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("raptors lets get it", submission.title, re.IGNORECASE):
            submission.reply("#insanity in toronto")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)

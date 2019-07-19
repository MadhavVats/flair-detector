import praw
from flask import Flask

# reddit = praw.Reddit(client_id='hhLD1xtDar8oCQ',
#                      client_secret='cQQVt0uucg6Ocl-wOoIlzEQJ3Ac', user_agent='reddit flair detector')
# hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
# for post in hot_posts:
#     print(post.title)

app = Flask(__name__)
 
@app.route('/')
def index():
   return 'ok'

if __name__ == "__main__":
    app.run()

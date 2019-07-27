from pymongo import MongoClient
import pymongo
import praw
from flask import Flask,render_template,request
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from pymongo import MongoClient
myclient = MongoClient(
    "mongodb+srv://Madhav:%2AAr%3C54jK@cluster0-b8qbz.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["data"]
mycol = mydb["stats2"]
stats={}
for document in mycol.find():
      flair_stat=document.copy()
      name=flair_stat['name']
      del flair_stat['_id']
      del flair_stat['name']
      stats[name]=flair_stat

model = joblib.load('model_joblib')
fitted_vectorizer = joblib.load('fitted_vectorizer')
app = Flask(__name__)
reddit = praw.Reddit(client_id='MwhK0qtk4ZqRdw', client_secret='cjytrTxD1OR4KtmEyZRk6wY7tfI', user_agent='flair' ,username='gcgvhjchvt2244')

@app.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
      link = request.form['link']
      submission = reddit.submission(url=link)
      comment = ''
      try:
            for top_level_comment in submission.comments:
                  comment += ' ' + top_level_comment.body
      except:
            pass
      data = submission.title + comment + submission.selftext
      ans = model.predict(fitted_vectorizer.transform([data]))
      return(render_template('pred.html',link=ans,stats=stats))
   return(render_template('index.html',stats=stats))
if __name__ == "__main__":
   app.run()


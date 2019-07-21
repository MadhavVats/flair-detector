import praw
from flask import Flask,render_template,request
from sklearn.externals import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
model = joblib.load('model_joblib')
fitted_vectorizer = joblib.load('fitted_vectorizer')
app = Flask(__name__)
reddit = praw.Reddit(client_id='MwhK0qtk4ZqRdw', client_secret='cjytrTxD1OR4KtmEyZRk6wY7tfI', user_agent='flair' ,username='gcgvhjchvt2244')

print(model.predict(fitted_vectorizer.transform([""""""])))
@app.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
      link = request.form['link']
      submission = reddit.submission(url=link)
      comment = ''
      for top_level_comment in submission.comments:
            comment += ' ' + top_level_comment.body
      data = submission.title + comment + submission.selftext
      return render_template('pred.html',link=data)
   return render_template('index.html')
if __name__ == "__main__":
   app.run()

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import praw\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     flairs                                             titles  upvotes  \\\n",
      "0  AskIndia  Need feedback for Insurance Policy that I took...        1   \n",
      "1  AskIndia   Somebody want to kill my full family what to do?       96   \n",
      "2  AskIndia  Ambassador of India takes back my newly issued...       13   \n",
      "3  AskIndia             [AskIndia] Cingari, Cengar or Tzengar?        0   \n",
      "4  AskIndia  Recommendations for books on Indian history wr...       16   \n",
      "\n",
      "       id                                                url  num_comms  \\\n",
      "0  1s57oi  https://www.reddit.com/r/india/comments/1s57oi...          1   \n",
      "1  b7pvwt  https://www.reddit.com/r/india/comments/b7pvwt...         24   \n",
      "2  bdfid1  https://www.reddit.com/r/india/comments/bdfid1...         27   \n",
      "3  18ntue  https://www.reddit.com/r/india/comments/18ntue...          0   \n",
      "4  avt1qx  https://www.reddit.com/r/india/comments/avt1qx...          9   \n",
      "\n",
      "        created                                            content  \\\n",
      "0  1.386254e+09  **Re-posting here because of lack of activity ...   \n",
      "1  1.554080e+09  It's now 24hrs, But local police station is no...   \n",
      "2  1.555361e+09  Hello /AskIndia!  First time poster, long time...   \n",
      "3  1.361085e+09  Hello,\\n\\nI submitted this to /r/rAskIndia a w...   \n",
      "4  1.551400e+09  Hello r/India.\\n\\nI'm British and would like t...   \n",
      "\n",
      "                     op                                           comments  \n",
      "0         dhavalcoholic   Dear Policy Holder(Dhavalcoholic),\\n \\nWe req...  \n",
      "1       amitkumarthakur   Calm down.\\nGo to the SP office of your town,...  \n",
      "2  FrustratedOCIHopeful   Honestly, she and her supervisor behaved *exa...  \n",
      "3             multubunu                                                     \n",
      "4         PoiHolloi2020   The Discovery of India by J.Nehru.\\n\\nYou wil...  \n"
     ]
    }
   ],
   "source": [
    "reddit = praw.Reddit(client_id='MwhK0qtk4ZqRdw', client_secret='cjytrTxD1OR4KtmEyZRk6wY7tfI', user_agent='flair' ,username='gcgvhjchvt2244')\n",
    "flairs_list = [\"AskIndia\", \"Non-Political\", \"[R]eddiquette\", \"Scheduled\", \"Photography\", \"Science/Technology\", \"Politics\", \"Business/Finance\", \"Policy/Economy\", \"Sports\", \"Food\", \"AMA\"]\n",
    "sub = reddit.subreddit('india')\n",
    "data_dict = {\"flairs\":[], \"titles\":[], \"upvotes\":[], \"id\":[], \"url\":[], \"num_comms\": [], \"created\": [], \"content\":[], \"op\":[], \"comments\":[]}\n",
    "\n",
    "for flair in flairs_list:\n",
    "    posts = sub.search(flair, limit=110)\n",
    "    for post in posts:\n",
    "        data_dict[\"flairs\"].append(flair)\n",
    "        data_dict[\"titles\"].append(post.title)\n",
    "        data_dict[\"upvotes\"].append(post.score)\n",
    "        data_dict[\"id\"].append(post.id)\n",
    "        data_dict[\"url\"].append(post.url)\n",
    "        data_dict[\"num_comms\"].append(post.num_comments)\n",
    "        data_dict[\"created\"].append(post.created)\n",
    "        data_dict[\"content\"].append(post.selftext)\n",
    "        data_dict[\"op\"].append(post.author)\n",
    "\n",
    "        post.comments.replace_more(limit=None)\n",
    "        comment = ''\n",
    "        for top_level_comment in post.comments:\n",
    "            comment += ' ' + top_level_comment.body\n",
    "        data_dict[\"comments\"].append(comment)\n",
    "\n",
    "data_df = pd.DataFrame(data_dict)\n",
    "print(data_df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(data_df['commments'], data_df['flair'], random_state= 0)\n",
    "\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer \n",
    " \n",
    "# settings that you use for count vectorizer will go here\n",
    "tfidf_vectorizer=TfidfVectorizer(use_idf=True)\n",
    " \n",
    "# just send in all your docs here\n",
    "tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(X_train)\n",
    " \n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

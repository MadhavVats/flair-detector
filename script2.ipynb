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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
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
    "X_train, X_test, y_train, y_test = train_test_split(data_df['commments'], data_df['flair'], random_state= 0)"
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

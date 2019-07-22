# flair-detector
### Overview
Flair detector is a web app that can detect the flair (category) of a Reddit post of the subreddit r/india.
### Directory structure
***templates :-*** Contains the necessary HTML pages to view the webpage.<br />
***Procfile :-*** Contains the command that is executed on the startup of heroku app.<br />
***data.json :-*** Contains the imported mongodb collection into json format.<br />
***fitted_factorizer :-*** Contains the saved vector that is used to transform the given input, to be able fit in the ML model.<br />
***model_joblib :-*** Contains the ML model.<br />
***requirements.txt :*** Contains the dependencies needed for heroku to build the web app.<br />
***script.py :-*** Contains the backend written with flask.<br />
***script2.ipynb :-*** This is the jupyter notebook in which the ML model was created and tested and the data was saved to the mongodb collection.<br />
### Dependencies
praw==6.3.1<br />
Flask==1.1.1<br />
itsdangerous==1.1.0<br /> 
Jinja2==2.10.1    <br /> 
gunicorn==19.9.0<br />
MarkupSafe==1.1.1<br />
Werkzeug==0.15.5<br />
sklearn==0.0 <br /> 
pymongo==3.8.0<br />
dnspython==1.16.0<br />
To run the run the program locally, type the command "python3 script.py" in the terminal.
### Approach used 

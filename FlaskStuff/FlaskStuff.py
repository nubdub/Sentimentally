import tweepy

#TextBlob is a Python Natural Language Processing Library
from textblob import TextBlob
from flask import Flask, render_template, request

app = Flask(__name__);

@app.route('/')
def index():
    return 'This is the home page'
 

@app.route('/profile/', methods=['POST'])
def profile():
    text = request.form['@twitter']
    consumer_key = 'TCNvmZhcLVgG66ktybasO6ZZQ'
    consumer_secret = '4n1AaDp8oSWMxJLaSz35WBlLuLgsyF7Xu8RYbfJAOkfBSy2UQF'
    access_token = '2607970348-zbW69Qxp55mHpd6oCacTulkN3QRuAONo1qSXbLI'
    access_token_secret = 'A6q3cgql3JQOdS05mDbOReuZ9EF3Q6ztbHRJAFGfMHy4v'

    #Tweepy API methods to scrape searched Tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #My weird text graphics lmao
    #print('-------------------------\n\nTwitter Sentiment Tool\n\nSentimental.ly\n\n-------------------------\n')
    #What the user desires to search
    stringtobesearched = text #input('What would you like to run the twitter sentiment analysis on?: ')

    #Tweepy API method to search inputted string
    public_tweets = api.search(stringtobesearched)

    #Polarity and Subjectivity on input
    polarityans = 0
    subjectivityans = 0
    count = 0
    tweetCounter = 0;
    sentiCounter = 0;
    tweetList = ['', '', '', '', '', '']
    sentimentList = ['', '', '', '', '', '']
    for tweet in public_tweets:
        tweetList.insert(tweetCounter, tweet.text)
        #tweetItself = tweet.text #print(tweet.text) #prints the tweet itself
        analysis = TextBlob(tweet.text)
        if (analysis.sentiment.subjectivity != 0 and analysis.sentiment.polarity != 0):
            subjectivityans += analysis.sentiment.subjectivity
            polarityans += analysis.sentiment.polarity
            count += 1
            sentimentList.insert(sentiCounter, analysis.sentiment)
            sentiCounter += 1
        tweetCounter += 1
    
    average1 = polarityans/count
    
    return render_template("profile.html", value=tweetList[0], value2=tweetList[1], value3=tweetList[2], value4=tweetList[3], value5=tweetList[4], value6=tweetList[5], senti=sentimentList[0], senti2=sentimentList[1], senti3=sentimentList[2], senti4=sentimentList[3], senti5=sentimentList[4], senti6=sentimentList[5], average=average1)
     

@app.route('/profile/')
def profile1():
    #searchText = request.form['@twitter']
    #tweet = "TEST"
    #tweet2 = "TEST2"
    #tweet3 = "TEST3"
    #tweet4 = "TEST4"
    #tweet5 = "TEST5"
    #tweet6 = "TEST6"
    
    #Twitter API keys and tokens to be used for Tweepy API
    consumer_key = 'TCNvmZhcLVgG66ktybasO6ZZQ'
    consumer_secret = '4n1AaDp8oSWMxJLaSz35WBlLuLgsyF7Xu8RYbfJAOkfBSy2UQF'
    access_token = '2607970348-zbW69Qxp55mHpd6oCacTulkN3QRuAONo1qSXbLI'
    access_token_secret = 'A6q3cgql3JQOdS05mDbOReuZ9EF3Q6ztbHRJAFGfMHy4v'

    #Tweepy API methods to scrape searched Tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #My weird text graphics lmao
    #print('-------------------------\n\nTwitter Sentiment Tool\n\nSentimental.ly\n\n-------------------------\n')
    #What the user desires to search
    stringtobesearched = "NBA" #input('What would you like to run the twitter sentiment analysis on?: ')

    #Tweepy API method to search inputted string
    public_tweets = api.search(stringtobesearched)

    #Polarity and Subjectivity on input
    polarityans = 0
    subjectivityans = 0
    count = 0
    tweetCounter = 0;
    sentiCounter = 0;
    tweetList = ['', '', '', '', '', '']
    sentimentList = ['', '', '', '', '', '']
    for tweet in public_tweets:
        tweetList.insert(tweetCounter, tweet.text)
        #tweetItself = tweet.text #print(tweet.text) #prints the tweet itself
        analysis = TextBlob(tweet.text)
        if (analysis.sentiment.subjectivity != 0 and analysis.sentiment.polarity != 0):
            subjectivityans += analysis.sentiment.subjectivity
            polarityans += analysis.sentiment.polarity
            count += 1
            sentimentList.insert(sentiCounter, analysis.sentiment)
            sentiCounter += 1
        tweetCounter += 1
    
    average1 = polarityans/count
    
    return render_template("profile.html", value=tweetList[0], value2=tweetList[1], value3=tweetList[2], value4=tweetList[3], value5=tweetList[4], value6=tweetList[5], senti=sentimentList[0], senti2=sentimentList[1], senti3=sentimentList[2], senti4=sentimentList[3], senti5=sentimentList[4], senti6=sentimentList[5], average=average1)

#@app.route('/<username>')
#def string(username):
#    return "Hello %s" % username

#@app.route('/<int:num>')
#def num(num):
#    return "The num is %s" % num

if __name__ == "__main__":
    app.run(debug=True);
    
 
    #polarityAndSubjectivity = analysis.sentiment #print(analysis.sentiment) #Prints polarity and subjectivity score
#print('-----------------------------------')
#print('\nResults for '+ stringtobesearched +':\n \nPOLARITY: ' + str(polarityans/count) + "\nSUBJECTIVITY: " + str(subjectivityans/count) + '\n')
#if((polarityans/count) > 0.1):
#    print('\nPositive by: '+ str(polarityans/count) + '\n')
#elif((polarityans/count) < 0.1):
#    print('\nNegative by: '+ str(polarityans/count) + '\n')
#else:
#    print('\nNetrual' + '\n')
#print('\n')
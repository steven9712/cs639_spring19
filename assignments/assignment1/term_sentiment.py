import sys
import re

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    scores = {}
    
    words = open(sentiment_file, 'r')
    for line in words:
        term, score = line.split("\t")
        scores[term] = int(score)

    words.close()
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0
    
    tweet = re.sub('\n', '', tweet)
    score = 0
    position = 0
    seperator = ' '
    phrase = []
    tweet = tweet.split(' ')
    i = 0
    k = 0
    diction = {}
    
    while (i < len(tweet)):
        flag = False
        position = 0
        word = tweet[i]
        phrase.append(word)
        
        for j in range(i+1, len(tweet)):
            phrase.append(tweet[j])
            seperator = seperator.join(phrase)

            if (seperator in sent_scores.keys()):
                position = j
                flag = True

            seperator = ' '

                
        if (flag == True):
            
            while (len(phrase) != (position - i + 1)):
                   phrase.pop() 
            word = seperator.join(phrase)
            if (word in sent_scores.keys()):
                score += int(sent_scores.get(word))
                diction[word] = int(sent_scores.get(word))
                i = position + 1
        else:
            if (phrase[0] in sent_scores.keys()):
                diction[phrase[0]] = int(sent_scores.get(phrase[0]))
                score += int(sent_scores.get(phrase[0]))
            else:
                diction[phrase[0]] = 0

            i = i+1
            
        seperator = ' '
        phrase.clear()
    new_diction = {}
    diction_len = len(diction)
    for key in diction:
        if (diction.get(key) == 0):
            new_diction[key] = score / diction_len
    
    return new_diction

def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    new_term_sent = {}
    
    tweets = open(tweets_file, 'r')
    for tweet in tweets:
        score = get_tweet_sentiment(tweet, sent_scores)

        for key in score:
            new_term_sent[key] = score.get(key)
            
    tweets.close()

    
    return new_term_sent


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    for term in new_term_sent:        
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()

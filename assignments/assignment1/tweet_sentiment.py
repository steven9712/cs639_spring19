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
    tweet = re.sub('\n', '', tweet)
    score = 0
    position = 0
    seperator = ' '
    phrase = []
    tweet = tweet.split(' ')
    i = 0
    k = 0
    
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
                i = position + 1
        else:
            if (phrase[0] in sent_scores.keys()):
                score += int(sent_scores.get(phrase[0]))

            i = i+1
            
        seperator = ' '
        phrase.clear()

    
    
    return score


def get_sentiment(tweets_file, sent_scores, output_file):
    """A function that finds the sentiment of each tweet and outputs a sentiment score (one per line).

            Args:
                tweets_file (string): The name of the file containing the clean tweets
                sent_scores (dictionary): The dictionary output by the method create_sent_dict
                output_file (string): The name of the file where the output will be written

            Returns:
                None
    """
    tweets = open(tweets_file, 'r')
    output = open(output_file, 'w')
    for tweet in tweets:
        score = get_tweet_sentiment(tweet, sent_scores)
        output.write('%d\n' % score)
    output.close()
    tweets.close()


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]
    output_file = "sentiment.txt"

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)
    # Read the tweet data and assign sentiment
    get_sentiment(tweets_file, sent_scores, output_file)


if __name__ == '__main__':
    main()

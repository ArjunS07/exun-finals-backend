"""
TODO: Fill in this file
- Use VADERSentiment to get the sentiment of a string

"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid_obj = SentimentIntensityAnalyzer()

TOO_NEG_THRESHOLD = -0.6

def get_str_sentiment(text: str) -> float:
    """Returns the sentiment of the text """

    sentiment_dict = sid_obj.polarity_scores(text)
    return sentiment_dict['compound']
    # TODO

def get_avg_list_sentiment(text_list: list) -> float:
    """Returns the average sentiment of all messages in a list using get_str_sentiment"""
    for x in text_list:
        sum_sentiment += get_str_sentiment(x)

    avg = sum_sentiment/len(text_list)
    return avg
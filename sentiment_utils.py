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


def get_user_messages(user_id: str) -> list:
    '''Gets all of the messages sent by a user'''
    # Don't worry about this for now
    # TODO: implement this function
    
def get_avg_user_sentiment(user_id: str) -> float:
    '''Gets the averge sentiment of the messages sent by a user'''
    messages = get_user_messages(user_id)
    user_sentiment = get_avg_list_sentiment(messages)
    return user_sentiment
    
def should_flag_user(user_id: str) -> bool:
    '''Returns true if the user's sentiment is too negative'''
    avg_sentiment = get_avg_user_sentiment(user_id)
    return avg_sentiment < TOO_NEG_THRESHOLD

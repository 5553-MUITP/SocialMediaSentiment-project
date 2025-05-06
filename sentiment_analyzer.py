# sentiment_analyzer.py

from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """Analyze sentiment of the given text and return the sentiment as 'Positive', 'Neutral', or 'Negative'."""
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity

    # Positive sentiment (greater than 0.05)
    if polarity > 0.05:
        return "Positive"
    
    # Negative sentiment (less than -0.05)
    elif polarity < -0.05:
        return "Negative"
    
    # Neutral sentiment (between -0.05 and 0.05)
    else:
        return "Neutral"

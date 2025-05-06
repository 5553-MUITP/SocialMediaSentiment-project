# test_sentiment_analyzer.py

import unittest
from sentiment_analyzer import analyze_sentiment  # Import the function to test

class TestSentimentAnalyzer(unittest.TestCase):
    
    def test_positive_sentiment(self):
        """Test if the function classifies positive sentiment correctly."""
        text = "I love this product!"
        result = analyze_sentiment(text)
        self.assertEqual(result, "Positive")

    def test_negative_sentiment(self):
        """Test if the function classifies negative sentiment correctly."""
        text = "Worst app ever made."
        result = analyze_sentiment(text)
        self.assertEqual(result, "Negative")

    def test_neutral_sentiment(self):
        """Test if the function classifies neutral sentiment correctly."""
        text = "It's okay, but really love it all."
        result = analyze_sentiment(text)
        self.assertEqual(result, "Positive")

    def test_edge_case_positive(self):
        """Test for sentiment that is slightly positive."""
        text = "I think this is great."
        result = analyze_sentiment(text)
        self.assertEqual(result, "Positive")

    def test_edge_case_negative(self):
        """Test for sentiment that is slightly negative."""
        text = "Not my favorite, hate it."
        result = analyze_sentiment(text)
        self.assertEqual(result, "Negative")
        
if __name__ == "__main__":
    unittest.main()

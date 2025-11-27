"""
Unit tests for sentiment_analysis module.
Tests the sentiment_analyzer function with positive, negative, and neutral inputs.
"""
import unittest
import os
from dotenv import load_dotenv

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

load_dotenv()

class TestSentimentAnalyzer(unittest.TestCase):
    """Test cases for sentiment_analyzer function."""

    @classmethod
    def setUpClass(cls):
        """Verify API credentials before running tests."""
        api_key = os.getenv('WATSON_API_KEY')
        url = os.getenv('WATSON_NLU_URL')
        
        if not api_key or not url:
            raise ValueError(
                "Missing WATSON_API_KEY or WATSON_NLU_URL in .env file. "
                "Tests cannot run without valid credentials."
            )

    def test_sentiment_analyzer(self):
        """Test sentiment analysis with positive, negative, and neutral texts."""
        # Test case for positive sentiment
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'positive')
        self.assertIsNotNone(result_1['score'])
        self.assertGreaterEqual(result_1['score'], 0.0)
        self.assertLessEqual(result_1['score'], 1.0)

        # Test case for negative sentiment
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'negative')
        self.assertIsNotNone(result_2['score'])
        self.assertGreaterEqual(result_2['score'], 0.0)
        self.assertLessEqual(result_2['score'], 1.0)

        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'neutral')
        self.assertIsNotNone(result_3['score'])
        self.assertGreaterEqual(result_3['score'], 0.0)
        self.assertLessEqual(result_3['score'], 1.0)


unittest.main()

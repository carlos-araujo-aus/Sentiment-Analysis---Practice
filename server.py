"""
Flask server for Sentiment Analysis application.
This module provides endpoints for analyzing text sentiment using Watson NLP.
"""
from flask import Flask, render_template, request

from SentimentAnalysis import sentiment_analyzer

app = Flask(__name__)  # ← ESTO ES IMPORTANTE

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Analyze sentiment of provided text."""
    text_to_analyze = request.args.get('textToAnalyze', '')
    
    # Validate input
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid input! Try again.", 400

    # Get sentiment analysis
    response = sentiment_analyzer(text_to_analyze)
    label = response.get('label')
    score = response.get('score')

    # Handle errors
    if label is None:
        return "Invalid input! Try again.", 500

    # Return formatted response
    return (
        f"The given text has been identified as " 
        f"<strong style='color: red;'>{label}</strong> with a score of "
        f"<strong style='color: red;'>{score}</strong> aout of 100."
    )

@app.route("/")
def render_index_page():
    """Render the main page."""
    return render_template('index.html')

@app.errorhandler(404)
def not_found(_error):
    """Handle 404 errors."""
    return "Page not found", 404

@app.errorhandler(500)
def internal_error(_error):
    """Handle 500 errors."""
    return "Internal server error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

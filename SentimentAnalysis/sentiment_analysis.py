"""
Sentiment analysis module using Watson NLP API.
Provides functionality to analyze text sentiment.
"""
import requests


def sentiment_analyzer(text_to_analyse):
    """
    Analyzes the sentiment of the given text using Watson NLP service.

    Args:
        text_to_analyse: Text string to analyze

    Returns:
        Dictionary with 'label' and 'score' keys
        Returns None values if analysis fails
    """
    url = ('https://sn-watson-sentiment-bert.labs.skills.network'
           '/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict')

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    headers = {
        "grpc-metadata-mm-model-id":
        "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    try:
        response = requests.post(url, json=payload, headers=headers,
                                 timeout=10)
        response.raise_for_status()

        data = response.json()

        return {
            'label': data['documentSentiment']['label'],
            'score': data['documentSentiment']['score']
        }

    except requests.exceptions.RequestException as error:
        print(f"Error during sentiment analysis: {error}")
        return {'label': None, 'score': None}

    except (KeyError, ValueError) as error:
        print(f"Error parsing response: {error}")
        return {'label': None, 'score': None}

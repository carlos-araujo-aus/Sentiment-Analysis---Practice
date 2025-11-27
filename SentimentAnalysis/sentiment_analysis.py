"""
Sentiment analysis module using Watson NLP API.
Provides functionality to analyze text sentiment.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def sentiment_analyzer(text_to_analyse):
    """
    Analyzes the sentiment of the given text using Watson NLP service.

    Args:
        text_to_analyse: Text string to analyze

    Returns:
        Dictionary with 'label' and 'score' keys
        Returns None values if analysis fails
    """
    url = os.getenv('WATSON_API_URL')
    api_key = os.getenv('API_KEY')
    watson_version = os.getenv('WATSON_VERSION')

    # Validar que existan las credenciales
    if not api_key or not url:
        print("Error: Missing WATSON_API_KEY or WATSON_NLU_URL in .env file")
        return {'label': None, 'score': None}
    
    params = {
        'version' : watson_version
    }

    print(text_to_analyse)

    payload = {
        "text": text_to_analyse,
        "features": {
            "sentiment" : {
                "document": True
            }
        }
    }

    headers = {
        "Content-Type" : "application/json"
    }

    try:
        response = requests.post(
            url, 
            json=payload,
            headers=headers,
            params=params, 
            auth=('apikey', api_key),
            timeout=10
            )
        response.raise_for_status()

        data = response.json()

        sentiment_data = data.get('sentiment', {}).get('document', {})

        row_score = abs(sentiment_data.get('score', 0.0))    
        score_porcentage= row_score *100
        score = f"{score_porcentage:.2f}"    
        label = sentiment_data.get('label', 'neutral')

        return {
            'label': label,
            'score': score
        }

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error during sentiment analysis: {error}")
        if response:
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")
        return {'label': None, 'score': None}

    except requests.exceptions.ConnectionError as error:
        print(f"Connection Error: Unable to reach Watson API - {error}")
        return {'label': None, 'score': None}

    except requests.exceptions.Timeout as error:
        print(f"Timeout Error: Watson API took too long to respond - {error}")
        return {'label': None, 'score': None}

    except requests.exceptions.RequestException as error:
        print(f"Error during sentiment analysis: {error}")
        return {'label': None, 'score': None}

    except (KeyError, ValueError) as error:
        print(f"Error parsing Watson NLU response: {error}")
        if 'response' in locals():
            print(f"Response data: {response.text}")
        return {'label': None, 'score': None}

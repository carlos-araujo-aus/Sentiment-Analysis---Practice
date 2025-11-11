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
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for 4xx/5xx status codes
        
        data = response.json()  
        
        return {
            'label': data['documentSentiment']['label'],
            'score': data['documentSentiment']['score']
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error during sentiment analysis: {e}")
        return {'label': None, 'score': None}
    
    except (KeyError, ValueError) as e:
        print(f"Error parsing response: {e}")
        return {'label': None, 'score': None}
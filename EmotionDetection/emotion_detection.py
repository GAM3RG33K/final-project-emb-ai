"""
This module performs emotion detection on a given text using Watson's BERT model.

The `emotion_detector` function takes in a string and 
    sends a POST request to the specified API URL. 
The response is then processed to extract relevant data & returned as json.

The `API_URL` constant holds the URL endpoint for
 the Watson BERT model emotion analysis service.

Dependencies:
- requests: To make HTTP POST requests to the API.

Example Usage:
```python
import emotion_detection

# Analyze a custom text
result = emotion_detection.emotion_detector("This is some example text.")

# Analyze default text
default_result = emotion_detection.emotion_detector()
"""

from typing import Dict
import requests

API = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

def format_response(data) -> Dict[str, str]:
    """This function formats the response from the API into a dictionary.

    Args:
        data (dict): The response from the API.

    Returns:
        dict: A dictionary containing the emotion scores and dominant emotion for the given text.
    """

    anger_score = float(data['anger'])
    disgust_score = float(data['disgust'])
    fear_score = float(data['fear'])
    joy_score = float(data['joy'])
    sadness_score = float(data['sadness'])

    dominant_emotion = max(data, key=data.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
def error_response(response) -> Dict[str, str]:
    """This function formats the error response from the API into a dictionary.

    Args:
        data (dict): The response from the API.

    Returns:
        dict: A dictionary containing the emotion scores and dominant emotion for the given text.
    """

    if response.status_code != 200:            
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            return {
                'error_message':  f'Something went wrong! Error={response.status_code}'
            }
    return None

def emotion_detector(input_text) -> Dict[str, str]:
    """emotion detection of the provided text 

    URL: f'{API}'
    Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input json: { "raw_document": { "text": input_text } }

    Returns:
        text: <string>
    """

    url = API
    myobj = { "raw_document": { "text": input_text } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)

    if error_response(response):
        return error_response(response)

    data = response.json()['emotionPredictions'][0]

    result =  format_response(data['emotion'])
    return result

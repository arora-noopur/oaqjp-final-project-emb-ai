import requests
import json

def emotion_detector(text_to_analyze):
    """
    Connects to the API to detect emotions, extracts scores, and finds the dominant emotion.
    Incorporates error handling for blank entries by checking the server's status code.

    Args:
        text_to_analyze (str): The text string to be analyzed for emotions.

    Returns:
        dict: A dictionary containing the scores for specific emotions and the dominant emotion,
              or a specific error structure if the request failed or input was blank.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # 1. Prepare the payload, even if blank
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        
        # 2. Check the status_code attribute
        if response.status_code == 200:
            # Successful response processing (Existing Logic)
            
            response_dict = response.json()
            emotion_scores = response_dict['emotionPredictions'][0]['emotion']
            
            # Extract required emotions and their scores
            anger_score = emotion_scores.get('anger', 0)
            disgust_score = emotion_scores.get('disgust', 0)
            fear_score = emotion_scores.get('fear', 0)
            joy_score = emotion_scores.get('joy', 0)
            sadness_score = emotion_scores.get('sadness', 0)

            # Determine the dominant emotion (highest score)
            emotion_map = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }

            dominant_emotion = max(emotion_map.items(), key=lambda x: x[1])[0]

            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        
        # 3. Error Handling using status_code
        else:
            # If the API call fails (non-200), we check if the input was blank.
            # Blank inputs often result in a 4xx error (Bad Request).
            if not text_to_analyze or response.status_code >= 400:
                 # Return a specific structure to signal the "blank entry" error to the server.py
                return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': 'Empty Entry' # Special flag
                }
            
            # Handle other, less specific API errors
            print(f"Error: API returned status code {response.status_code}. Response text: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error processing API response structure: {e}")
        return None
import requests
import json

def emotion_detector(text_to_analyze):
    """
    Connects to the API to detect emotions, extracts scores, and finds the dominant emotion.

    Args:
        text_to_analyze (str): The text string to be analyzed for emotions.

    Returns:
        dict: A dictionary containing the scores for specific emotions and the dominant emotion,
              or None if the request was unsuccessful or input is invalid.
    """
    # 1. Define the API endpoint and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Handle empty or invalid input text
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # 2. Make the POST request to the API
    try:
        response = requests.post(url, headers=headers, json=input_json)
        
        # 3. Check for successful response status (HTTP 200)
        if response.status_code == 200:
            # Convert response text to a dictionary using json.loads() 
            # (though response.json() is often simpler and used here)
            response_dict = response.json()
            
            # Navigate to the emotion scores
            emotion_scores = response_dict['emotionPredictions'][0]['emotion']
            
            # 4. Extract required emotions and their scores
            anger_score = emotion_scores.get('anger', 0)
            disgust_score = emotion_scores.get('disgust', 0)
            fear_score = emotion_scores.get('fear', 0)
            joy_score = emotion_scores.get('joy', 0)
            sadness_score = emotion_scores.get('sadness', 0)

            # 5. Determine the dominant emotion (highest score)
            
            # Create a dictionary of the target emotions and their scores
            emotion_map = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }

            # Find the emotion with the maximum score
            # The key=lambda... function tells max() to compare the values (scores)
            dominant_emotion = max(emotion_map.items(), key=lambda x: x[1])[0]

            # 6. Return the required output format
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        
        # Handle cases where the request failed
        else:
            print(f"Error: API returned status code {response.status_code}. Response text: {response.text}")
            # For failed analysis, return None scores
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error processing API response structure: {e}")
        return None
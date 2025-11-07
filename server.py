"""
Flask web server for running the Emotion Detection application.

This module handles web requests, calls the external emotion_detector function, 
and returns the processed result or appropriate error messages.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application (renamed to APP for Pylint compliance)
APP = Flask("Emotion Detector")

@APP.route("/")
def render_index_page():
    """Renders the main HTML page (index.html)."""
    # Flask automatically looks in the 'templates' folder for index.html
    return render_template('index.html')

@APP.route("/emotionDetector")
def emotion_detector_route():
    """
    Handles the request for emotion detection, processes the text, 
    and returns the result in the required output format.
    
    Returns:
        str: A formatted message string with emotion scores and dominant emotion,
             or an error message if analysis fails.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Check for complete failure (e.g., API connection error returning None)
    if response is None:
        return "An error occurred during API analysis. Please try again later."
    dominant_emotion = response.get('dominant_emotion')
    # Check for processing errors: None means analysis failed; 'Empty Entry' means blank input.
    if dominant_emotion is None or dominant_emotion == 'Empty Entry':
        # Returns the required message for invalid or blank text input.
        return "Invalid text! Please try again."
    # Construct the final output string by accessing response dict directly
    # (Fixes Pylint R0914 - Too many local variables, and C0301 - Line too long)
    output_message = (
        f"For the statement '{text_to_analyze}', "
        f"the dominant emotion is **{dominant_emotion}**."
        f" The scores are: 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, and "
        f"'sadness': {response['sadness']}."
    )
    return output_message
if __name__ == "__main__":
    # Run the application on a local host and port 5000 (default)
    APP.run(host="0.0.0.0", port=5000)
    
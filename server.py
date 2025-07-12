"""
Flask web server for Emotion Detection application.

Provides routes to render main page and analyze emotions from user input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detect_route():
    """
    Detect emotion from given text input and return formatted result.

    Returns:
        str: Formatted string describing emotion scores and dominant emotion,
             or an error message for invalid input.
    """
    if request.method == 'POST':
        text = request.form.get('text', '')
    else:
        text = request.args.get('textToAnalyze', '')

    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return formatted_result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

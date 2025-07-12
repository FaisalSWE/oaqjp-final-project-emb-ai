# Emotion Detection Application

This project implements an emotion detection system using IBM Watson NLP's Emotion Predict API, wrapped in a Flask web application.

## Features

- Analyze emotions (anger, disgust, fear, joy, sadness) from input text
- Returns dominant emotion with scores for each emotion
- Handles blank inputs gracefully with error messages
- Web interface built with Flask for easy user interaction

## Project Structure

- `EmotionDetection/` - Python package containing the emotion detection logic
- `server.py` - Flask web server for deployment
- `templates/index.html` - Main HTML page for user input (provided)
- `static/mywebscript.js` - JavaScript for frontend interactions (provided)
- `test_emotion_detection.py` - Unit tests for emotion detection functionality

## How to Run

1. Clone the repository and navigate to the project folder.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
   (Ensure requests and flask are installed)
3. Run the Flask server:
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```
4. Open the web interface in your browser:
   ```arduino
   http://localhost:5000
   ```
5. Enter text to analyze emotions.
## Testing
Run unit tests with:
```bash
python3 test_emotion_detection.py
```
## Code Quality
Static code analysis is performed using PyLint to maintain a clean codebase with a 10/10 score.

## Author
FaisalSWE

## License
Apache License
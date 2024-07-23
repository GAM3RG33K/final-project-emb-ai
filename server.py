''' Executing this function initiates the application of emotion detection 
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the score of emotions and the dominant emotion.
    '''

    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return {"error": "No text provided to process"}, 400

    result = emotion_detector(text_to_analyze)

    if 'error_code' in result:
        return {"error": f"The given text is unprocessed due to server error = {result['error_code']}"}, 500

    return f"""For the given statement, the system response is 
        'anger': {result['anger']}, 
        'disgust': {result['disgust']},
        'fear': {result['fear']},
        'joy': {result['joy']} 
        and 'sadness': {result['sadness']}. 
        
        The dominant emotion is {result['dominant_emotion']}."""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

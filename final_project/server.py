
"""Flask web application for IBM Watson emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/")
def home():
    """Render the emotion detection homepage."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyse user text and return the predicted emotions."""
    text = request.args.get("textToAnalyze", "")

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
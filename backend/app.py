from flask import Flask, request, jsonify
from emotion_detection import detect_emotions
from sentiment_analysis import analyze_sentiments
from keyword_analysis1 import extract_keywords_with_themes, extract_significant_keywords
from insight_generation import generate_actionable_insights

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_comments():
    data = request.json
    comments = data.get("comments", [])

    if not comments:
        return jsonify({"error": "No comments provided"}), 400

    # Call the functionalities
    emotion_results = detect_emotions(comments)
    sentiment_percentages = analyze_sentiments(comments)
    # keyword_results = extract_keywords(comments)
    keyword_results = extract_significant_keywords(comments)
    keyword_themes = extract_keywords_with_themes(comments, num_clusters=3)
    emotion_frequencies = {}
    total_emotions = 0

    actionable_insights=generate_actionable_insights(keyword_themes)

    # Iterate over each result from detect_emotions
    for result in emotion_results:
        # Calculate the total score for this comment to normalize
        comment_total_score = sum(emotion["score"] for emotion in result["emotions"])

        for emotion in result["emotions"]:
            emotion_name = emotion["label"]
            # Normalize the score before adding to frequencies
            normalized_score = emotion["score"] / comment_total_score if comment_total_score > 0 else 0
            emotion_frequencies[emotion_name] = emotion_frequencies.get(emotion_name, 0) + normalized_score
            total_emotions += normalized_score

    # Calculate percentages
    emotion_percentages = {
        emotion: (score / total_emotions) * 100 for emotion, score in emotion_frequencies.items() if total_emotions > 0
    }

    response = {
        # "emotions": emotion_results,
        "emotion_percentages": emotion_percentages,
        "sentiment_percentages": sentiment_percentages,
        "keywords": keyword_results,
        "keyword_themes": keyword_themes,
        "actionable_insights": actionable_insights
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

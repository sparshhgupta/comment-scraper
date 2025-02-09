from transformers import pipeline

# Initialize the emotion detection model
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def detect_emotions(comments):
    """Detect emotions in a list of comments."""
    results = []
    for comment in comments:
        emotions = emotion_model(comment)
        sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)
        results.append({
            "text": comment,
            "emotions": sorted_emotions[:3]  # Top 3 emotions
        })
    return results

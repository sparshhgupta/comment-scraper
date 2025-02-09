from transformers import pipeline

# Initialize the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiments(comments):
    """Analyze sentiment percentages (positive, negative, neutral) for a list of comments."""
    # Initialize counts with consistent labels
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    total_comments = len(comments)

    for comment in comments:
        # Get sentiment prediction
        sentiment = sentiment_model(comment)[0]
        label = sentiment['label'].lower()  # Normalize label to lowercase

        # Map labels to our dictionary keys
        if "pos" in label:
            sentiment_counts["Positive"] += 1
        elif "neg" in label:
            sentiment_counts["Negative"] += 1
        elif "neutral" in label:  # Handle models that may have "Neutral"
            sentiment_counts["Neutral"] += 1
        else:
            # For unexpected labels, categorize as "Neutral" by default
            sentiment_counts["Neutral"] += 1

    # Calculate percentages
    percentages = {label: (count / total_comments) * 100 for label, count in sentiment_counts.items()}
    return percentages

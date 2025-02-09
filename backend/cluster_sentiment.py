from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_analysis_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
    """Returns sentiment using a transformer model for the given text."""
    # Perform sentiment analysis using the transformer model
    result = sentiment_analysis_pipeline(text)
    
    # Extract the sentiment label
    sentiment_label = result[0]['label']  # 'POSITIVE' or 'NEGATIVE'
    
    return sentiment_label.lower()  # Convert to lowercase for consistency

def aggregate_theme(theme_keywords):
    """
    Aggregate the keywords for a theme into a string and analyze its sentiment.
    
    Args:
        theme_keywords (list): List of keywords for the theme.
        
    Returns:
        str: Sentiment of the aggregated theme.
    """
    # Aggregate the theme keywords into a single string
    aggregated_text = " ".join(theme_keywords)
    
    # Get the sentiment of the aggregated text)
    
    return aggregated_text

def analyze_all_themes(keyword_themes):
    """
    Analyze sentiment for all themes in the keyword_themes dictionary.
    
    Args:
        keyword_themes (dict): A dictionary containing themes and their associated keywords.
        
    Returns:
        dict: A dictionary with themes and their sentiment analysis.
    """
    theme_sentiments = {}
    
    for theme, keywords in keyword_themes.items():
        aggreated_theme = aggregate_theme(keywords)
        theme_sentiments[theme] = get_sentiment(aggreated_theme)
    
    return theme_sentiments
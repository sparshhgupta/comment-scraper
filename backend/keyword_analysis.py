import spacy
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter

# Initialize the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(comments):
    """Extract most frequent keywords across all comments."""
    all_text = " ".join(comments)
    doc = nlp(all_text)
    lemmatized_keywords = [
        token.lemma_ for token in doc if token.is_alpha and not token.is_stop
    ]
    keyword_frequencies = Counter(lemmatized_keywords)
    return keyword_frequencies.most_common(10)


# THIS FUNCTION CLUSTERS ALL THE WORDS NOT ONLY KEYWORDS
# def extract_keywords_with_themes(comments, num_clusters=3):
#     """
#     Extract keywords and cluster them into themes using KMeans.
    
#     Args:
#         comments (list of str): List of comments.
#         num_clusters (int): Number of clusters/themes.
    
#     Returns:
#         dict: Clustered themes with associated keywords and frequencies.
#     """
#     # Flatten all comments into a single text
#     all_text = " ".join(comments)
    
#     # Tokenize and count keyword frequencies
#     words = all_text.split()
#     keyword_counts = Counter(words)
#     keywords = [keyword for keyword, freq in keyword_counts.items() if len(keyword) > 2]  # Filter short words
    
#     # Create a TF-IDF vectorizer
#     vectorizer = TfidfVectorizer(stop_words="english")
#     keyword_vectors = vectorizer.fit_transform(keywords)
    
#     # Apply KMeans clustering
#     kmeans = KMeans(n_clusters=num_clusters, random_state=42)
#     clusters = kmeans.fit_predict(keyword_vectors)
    
#     # Map keywords to their clusters
#     clustered_keywords = {i: [] for i in range(num_clusters)}
#     for keyword, cluster in zip(keywords, clusters):
#         clustered_keywords[cluster].append((keyword, keyword_counts[keyword]))
    
#     # Organize results as themes
#     themes = {}
#     for cluster, items in clustered_keywords.items():
#         sorted_items = sorted(items, key=lambda x: x[1], reverse=True)  # Sort by frequency
#         themes[f"Theme {cluster + 1}"] = sorted_items
    
#     return themes

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from textblob import TextBlob
from collections import Counter
from rake_nltk import Rake

from sklearn.metrics import silhouette_score

def determine_clusters_with_silhouette(keywords, max_clusters=10):
    vectorizer = TfidfVectorizer(stop_words="english")
    keyword_vectors = vectorizer.fit_transform(keywords)

    silhouette_scores = []
    for k in range(2, max_clusters + 1):  # Silhouette requires at least 2 clusters
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(keyword_vectors)
        score = silhouette_score(keyword_vectors, labels)
        silhouette_scores.append((k, score))

    best_k = max(silhouette_scores, key=lambda x: x[1])[0]

    print(f"Optimal number of clusters based on Silhouette Score: {best_k}")
    return best_k, silhouette_scores


def extract_significant_keywords(comments):
    """Extract significant keywords using RAKE."""
    all_text = " ".join(comments)
    
    # Initialize RAKE with NLTK stopwords
    r = Rake()  # You can customize stopwords if needed
    
    # Extract keywords from text
    r.extract_keywords_from_text(all_text)
    ranked_phrases = r.get_ranked_phrases_with_scores()  # Returns (score, phrase) tuples
    
    # We will use the ranked phrases (ignoring scores for now)
    keywords = [phrase.lower() for score, phrase in ranked_phrases]
    
    # Count frequencies
    keyword_counts = Counter(keywords)
    
    top_keywords = keyword_counts.most_common(40)

    # Convert to dictionary for further processing
    filtered_keywords = {word: freq for word, freq in top_keywords if len(word) > 2}  # Filter short words  

    return filtered_keywords

    # Filter low-frequency words (e.g., occurring <2 times)
    # filtered_keywords = {word: freq for word, freq in keyword_counts.items() if freq > 1}

    # return filtered_keywords

# def extract_significant_keywords(comments):
#     """Extract significant keywords using TextBlob."""
#     all_text = " ".join(comments)
#     blob = TextBlob(all_text)

#     # Extract nouns, noun phrases, and verbs
#     keywords = []
#     for word, pos in blob.tags:
#         if pos.startswith("NN") or pos.startswith("VB"):  # Nouns and Verbs
#             keywords.append(word.lower())

#     # Count frequencies
#     keyword_counts = Counter(keywords)
    
#     # Filter low-frequency words (e.g., occurring <2 times)
#     filtered_keywords = {word: freq for word, freq in keyword_counts.items() if freq > 1}

#     return filtered_keywords

def cluster_keywords_by_themes(filtered_keywords, num_clusters=3):
    """Cluster significant keywords into themes using KMeans."""
    keywords = list(filtered_keywords.keys())
    num_clusters,_=determine_clusters_with_silhouette(keywords)
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words="english")
    keyword_vectors = vectorizer.fit_transform(keywords)

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(keyword_vectors)

    # Map keywords to their clusters
    clustered_keywords = {i: [] for i in range(num_clusters)}
    for keyword, cluster in zip(keywords, clusters):
        clustered_keywords[cluster].append((keyword, filtered_keywords[keyword]))

    # Organize results as themes
    themes = {}
    for cluster, items in clustered_keywords.items():
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)  # Sort by frequency
        themes[f"Theme {cluster + 1}"] = sorted_items

    return themes

def extract_keywords_with_themes(comments, num_clusters=3):
    """
    Extract keywords and cluster them into themes.
    Combines keyword extraction with clustering.
    """
    # Step 1: Extract significant keywords
    filtered_keywords = extract_significant_keywords(comments)

    # Step 2: Cluster the keywords
    themes = cluster_keywords_by_themes(filtered_keywords, num_clusters)

    return themes


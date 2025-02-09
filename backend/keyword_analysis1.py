from sklearn.cluster import KMeans
from collections import Counter
from rake_nltk import Rake
from sklearn.metrics import silhouette_score
from sentence_transformers import SentenceTransformer

# Load the pre-trained Sentence Transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def determine_optimal_clusters(embeddings, max_clusters=10):
    """
    Determine the optimal number of clusters using silhouette score.
    """
    best_k = 2
    best_score = -1

    for k in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        clusters = kmeans.fit_predict(embeddings)
        score = silhouette_score(embeddings, clusters)

        if score > best_score:
            best_k = k
            best_score = score

    return best_k

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

def generate_embeddings(keywords):
    """
    Generate embeddings for a list of keywords using Sentence Transformers.
    Ensure keywords is a list of strings.
    """
    # Ensure keywords is a list of strings
    if not isinstance(keywords, list):
        raise ValueError("Keywords should be a list of strings.")

    embeddings = model.encode(keywords, show_progress_bar=True)
    return embeddings


def cluster_keywords_with_embeddings(keywords, num_clusters=3):
    """
    Cluster keywords using embeddings and KMeans.
    """
    # Generate embeddings for keywords
    embeddings = generate_embeddings(keywords)

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(embeddings)

    # Organize keywords by their clusters
    clustered_keywords = {i: [] for i in range(num_clusters)}
    for keyword, cluster in zip(keywords, clusters):
        clustered_keywords[cluster].append(keyword)

    # Return organized clusters
    themes = {f"Theme {i + 1}": clustered_keywords[i] for i in clustered_keywords}
    return themes

def cluster_keywords_with_embeddings_dynamic(keywords, max_clusters=10):
    """
    Cluster keywords dynamically using embeddings and optimal number of clusters.
    """
    embeddings = generate_embeddings(keywords)
    num_clusters = determine_optimal_clusters(embeddings, max_clusters)

    # Cluster with the optimal number of clusters
    return cluster_keywords_with_embeddings(keywords, num_clusters)

def extract_keywords_with_themes(comments, num_clusters=3):
    """
    Extract keywords and cluster them into themes.
    Combines keyword extraction with clustering.
    """
    # Step 1: Extract significant keywords
    filtered_keywords = extract_significant_keywords(comments)
    filtered_keywords = list(filtered_keywords.keys())
    # Step 2: Cluster the keywords
    themes = cluster_keywords_with_embeddings_dynamic(filtered_keywords)

    return themes
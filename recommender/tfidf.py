import time

from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

def trainEngine(plots):
    start= time.time()
    # Initializing tf-idf vectorizer
    vectorizer = TfidfVectorizer(
        lowercase=True,
        min_df=3,
        max_df=0.95,
        ngram_range=(1,2),
        stop_words='english')
    plotsTFIDF=vectorizer.fit_transform(plots)
    return plotsTFIDF

def getSimilarities(id, recommendations, plotsTFIDF):
    start = time.time()
    # Generate cosine similarities
    cosineSimilarities = linear_kernel(plotsTFIDF, plotsTFIDF)
    # Get similarity scores for the input movie
    scores = list(enumerate(cosineSimilarities[id]))
    # Sort into descending order the scores
    sortedScores = sorted(scores, key=lambda x: x[1], reverse=True)
    # Get the number of the recommendations asked
    movieRecommendations = sortedScores[1:recommendations + 1]
    # Get the indices of the recommendation movies
    movieIndices = [i[0] for i in movieRecommendations]
    return movieIndices
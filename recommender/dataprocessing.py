import sys
import time
import pandas as pd
import logging
import unicodedata
from  __builtin__ import any as b_any

from os.path import join,dirname

parentPath = dirname(__file__)
moviesCSVPath = join(parentPath,'dataset/movie_metadata.csv')

def getImages():
    movies = pd.read_csv(moviesCSVPath)
    images = movies[['movie_poster']].values.flatten().tolist()
    return images
    
def importData():
    start= time.time()
    # Import movie dataset
    moviesDF = pd.read_csv(moviesCSVPath)
    logging.info("Reading data from file movie_metadata.csv")
    # Return movies dataframe
    return moviesDF

def splitData(moviesDF):
    start = time.time()
    # Get movie titles
    titles = moviesDF[['movie_title']].values.flatten().tolist()
    # Get movie genres
    categories = moviesDF[['genres']].values.flatten().tolist()
    # Get movie plot summaries
    plot = moviesDF[['movie_plot']].values.flatten().tolist()
    # Get movie posters
    posters = moviesDF[['movie_poster']].values.flatten().tolist()
    # Pack and return the split data
    logging.info("Splitting data")
    return {'titles': titles,'categories':categories, 'plots':plot,'posters':posters}

def validateMovieID(movieID):
    #Check whether the input ID is valid
    if not (isinstance(movieID, int) and movieID >= 0 and movieID <= 5050):
        sys.exit(1)
    return 0

def validateRecommendations(recommendationsNumber):
    # Check whether the recommendations number is valid
    if not (isinstance(recommendationsNumber, int)
            and recommendationsNumber >= 1 and recommendationsNumber <= 30):
        sys.exit(1)
    return 0

def validateLength(length):
    # Check whether the list length is valid
    if not (isinstance(length, int) and length >= 1 and length <= 5000):
        sys.exit(1)
    return 0

def validateInput(movieID, recommendationsNumber):
    # Check whether the user input is valid
    validateMovieID(movieID)
    validateRecommendations(recommendationsNumber)
    return 0

def searchMovie(movieID):
    # Check whether the input ID is valid
    validateMovieID(movieID)
    # Search a movie title by ID
    data = importData()
    dataset = splitData(data)
    # Display the search result
    print(
        "Movie ID",movieID,
        "Title:",dataset['titles'][movieID],
        "Genres:",dataset['categories'][movieID],
        "Plot",dataset['plots'][movieID])
       # showPlots=False)

def findId(movie_name, dataset):
    decoded=[str(x).decode('UTF8') for x in dataset['titles']]
    encoded=[x.encode('ascii','replace') for x in decoded]

    lower_encoded=[x.lower() for x in encoded]
    if b_any(movie_name.lower() in x.lower() for x in encoded):
        index = lower_encoded.index(movie_name.lower())
        return index
    else:
        return 1



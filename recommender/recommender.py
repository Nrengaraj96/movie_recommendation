from dataprocessing import importData, splitData, validateInput
from tfidf import trainEngine, getSimilarities


def recommender(movieId,recommendationsNumber):
    #Validate the user input
    validateInput(movieId, recommendationsNumber)
    #Import the data
    data = importData()
    # Get the metadatasets
    dataset = splitData(data)
    #Convert to unicode objects
    decoded=[str(x).decode('UTF8') for x in dataset['plots']]
    # Train the recommendation engine
    results = trainEngine(map(unicode, decoded))
    # Generate recommendations
    recomendedMovies = getSimilarities(movieId, recommendationsNumber, results)

    reco_list=[(movieId,dataset['titles'][movieId],dataset['categories'][movieId],dataset['plots'][movieId],dataset['posters'][movieId])]

    for i in recomendedMovies:
        reco_list.append((i, dataset['titles'][i],dataset['categories'][i],dataset['plots'][i],dataset['posters'][i]))
    return reco_list
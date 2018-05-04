from recommender import recommender
from dataprocessing import findId,importData,splitData
import json



def main(movieId):
    reco= recommender(movieId=movieId,
        recommendationsNumber=3)
    return reco

if __name__ == '__main__':
    DataFrame=importData()
    datas=splitData(DataFrame)
    movie_name= query['query']['bool']['should'][0]['match']['movie_title']
    qmark='?'
    movieId =findId(movie_name+qmark, datas)

    recommended= main(movieId)
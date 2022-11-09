import random
import pandas as pd

movies = pd.read_csv("df_rcommendations.csv")

def random_recommender():
    recommendations= list(movies.query("rating >= 4")["title"])
    random.shuffle(recommendations)
    return recommendations[:10]

if __name__=='__main__':
    top10 = random_recommender()
    print(top10)

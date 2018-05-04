import sys
import time
import pandas as pd


from os.path import join, dirname

parentPath = dirname(__file__)
moviesCSVPath = join(parentPath,'dataset/movie_metadata.csv')

movies= pd.read_csv(moviesCSVPath)
images= movies[['movie_poster']].values.flatten().tolist()
titles = movies[['movie_title']].values.flatten().tolist()

print len(images)

for i in range(len(images)):
    f= open("imgsrc.txt","a")
    f.write("<div class='gallery' style ='float:left;'>\n <a target='_blank' href='{0}'>\n<img src='{0}' alt='{1}' width='200' height='100'>\n</a>\n<div class='desc'>{2}</div>\n</div>\n".format(images[i],titles[i],i))
    f.close()

    
    
    
    
 

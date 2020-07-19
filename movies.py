import pandas as pd 
import numpy as np
import time
from selenium import webdriver


movie = pd.read_csv('/Users/mohammedkhaddam/Desktop/movies/movies.csv')

crit= movie.content_rating=='PG-13'

crit1= movie.imdb_score >= 8 

crit3 = movie.title_year >= 1990
final=   crit & crit1 & crit3

movie['final']= final
final1=np.array(final)
x=movie[['movie_title',
        'final']].dropna()
#np.where(x["final"] == True)


select_movie = list(np.where(x["final"] == True)[0])

pick_one=x.iloc[select_movie]
y= np.array(pick_one['movie_title'])
pick_random_one = np.random.choice(y)
print(pick_random_one)

#link ="https://google.com/" + str(pick_random_one)
driver = webdriver.Chrome('/Users/mohammedkhaddam/Desktop/movies/chromedriver')


driver.get("http://google.com")
driver.maximize_window()
time.sleep(5)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys(pick_random_one)
inputElement.submit()
time.sleep(5)
try:
   elem = driver.find_element_by_partial_link_text("Netflix")
   elem.click()
except : 
    print("Sorry not existed on Netflix")
#time.sleep(20)

#driver.close()
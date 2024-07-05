# 109550186
# GUI using Tkinter
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import psycopg2
import numpy as np
import matplotlib.pyplot as plt

# use sklearn count vectorizer to get recommendations
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

############################################# GUI part #############################################
root = Tk()
root.title('Netflix Recommendation Movies and TV Shows --- Database Final Project')

# Create submit function
def submit():
    # get value from text box
    mname = movie_name.get()

    ############################# DATABASE AND APPLICATION INTEGRATION #############################

    # connecting to database
    ENDPOINT = "database-finalproject.ckfwjyvsvorx.us-east-1.rds.amazonaws.com"
    PORT = 5432
    DBNAME = "netflix_data"
    USER = "postgres"
    token = "cindyvvv" 

    # database connection
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USER, password=token)
    print("Database opened successfully")

    # data in <class 'pandas.core.frame.DataFrame'> type
    dataframe = pd.read_sql("select * from details", conn)

    # deal with the data
    # 1. filling null values with empty string
    filled = dataframe.fillna('')

    # 2. cleaning the data - lowercase all the words
    def lcase(x):
        return str.lower(x.replace(" ", ""))

    # factors which the model based on recommending
    factors = ['title', 'director', 'casts', 'listed_in', 'description']
    filled = filled[factors]

    for factor in factors:
        filled[factor] = filled[factor].apply(lcase)

    # create soup or bag of words for all rows
    def createsoup(x):
        return x['title']+ ' ' + x['director'] + ' ' + x['casts'] + ' ' +x['listed_in']+' '+ x['description']
    filled['soup'] = filled.apply(createsoup, axis=1)

    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(filled['soup'])

    cosinesim = cosine_similarity(count_matrix, count_matrix)

    filled = filled.reset_index()
    indices = pd.Series(filled.index, index=filled['title'])

    def getrecommendations(title, cosine_sim=cosinesim):
        title = title.replace(' ','').lower()
        index = indices[title]

        # similarity scores of the inputted movie with others
        sim_scores = list(enumerate(cosine_sim[index]))

        # sort movies based on the scores and get the top 10 most similar ones
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]

        # get movie indices
        movie_indices = [i[0] for i in sim_scores]

        # get the top 10 movies titles
        topten = dataframe['title'].iloc[movie_indices].values

        # convert ndarray to list then to string
        res = ''
        toptenlist = []
        toptenlist = topten.tolist()
        for i in range(0, 10):
            res = "\n".join(toptenlist)

        # return the top 10 most similar movies in string
        return res

    ################################################################################################
    try:
        recom = getrecommendations(mname, cosinesim)
        Label(root, text="Top 10 Recommendations:", font=('Calibri 10'), justify=LEFT, anchor="w").grid(row=6, column=0, padx=10, sticky=W)
        Label(root, text=recom, font=('Calibri 10'), justify=LEFT, anchor="w").grid(row=6, column=1, padx=10, sticky=W)
    except KeyError:
        print("Inputted value not in Netflix.\nPlease input other movie or show.")
        movie_name.delete(0, END)
    
    # commit changes
    conn.commit()

    # clear the text boxes
    movie_name.delete(0, END)

# Create text boxes
movie_name = Entry(root, width = 30)
movie_name.grid(row=0, column=1, padx=20)

# Create text box lables
movie_name_label = Label(root, text="Movie or Shows Name", justify=LEFT).grid(row=0, column=0, padx=10)

# Create submit button
submit_btn = Button(root, text="Show recommendations", command=submit)
submit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()

####################################################################################################
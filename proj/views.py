from . import app
from flask import render_template
from . import  movie
from . import request

@app.route('/')
def home():
    movies=[]
    for i in range(11):
        req=request.Request()
        data=req.request("https://api.themoviedb.org/3/movie/{}?api_key=39629360e6a9369540ad0e2fe3cc84d6",500+i)
        movies.append(movie.Movie(data["id"],data["title"],data["overview"],data["poster_path"],data["vote_average"],data["vote_count"]))
        


    return render_template('index.html',datum=movies)
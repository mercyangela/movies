import os
import json
import urllib.request
from flask import Flask, request, g, redirect, abort, \
     render_template, flash

#Create application
app = Flask(__name__)
app.config.from_object(__name__)

def load_movies():
    json_data = urllib.request.urlopen("http://kolastudios.com/internship/ester/get_movies.php").readall().decode('utf-8')
    data = json.loads(json_data)
    return data['movies']

#if __name__ == '__main__':
#    app.run()

@app.route('/')
def show_entries():
    entries = load_movies()
    return render_template('show_entries.html', entries=entries)

@app.route('/details/')
def details():
    entries = load_movies()
    m = {"Title":"None", "Content":"none"}
    #print(request.args["id"])
    for movie in entries:
        if str(movie["id"]) == str(request.args["id"]):
            m = movie
    return render_template('show_details.html', entry=m)

if __name__=="__main__":
    app.run()

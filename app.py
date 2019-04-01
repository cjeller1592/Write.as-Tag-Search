from flask import Flask, request, redirect, url_for, flash, render_template
from tags import retrieveTags
from forms import search

import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def tagSearch():
    form = search()
    if request.method == 'POST':
        collection = request.form['collection']
        tags = retrieveTags(collection)
        flash(tags)
        return redirect(url_for('tagSearch'))

    return render_template('search.html', form=form)

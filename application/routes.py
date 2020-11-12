from flask import Flask, render_template, url_for, redirect, request
from application import app, db
from application.models import Listing, Category
from application.forms import ListingForm

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = ListingForm()
    if form.validate_on_submit():
        lister = Listing(
            title = form.title.data,
            list_description = form.list_description.data,
            categories = form.categories.data
        )
        db.session.add(lister)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)



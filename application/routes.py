from flask import Flask, render_template, url_for, redirect, request
from application import app, db
from application.models import Listing, Detail
from application.forms import ListingForm, DetailForm

@app.route('/', methods=['POST', 'GET'])
def index():
    all_listing = Listing.query.all()
    return render_template('index.html', all_listing=all_listing)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = ListingForm()
    if form.validate_on_submit():
        lister = Listing(
            list_title = form.list_title.data,
            list_location = form.list_location.data,
            list_price = form.list_price.data
        )
        db.session.add(lister)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form  = ListingForm()
    listing = Listing.query.get(id)
    if form.validate_on_submit():
        list_title = form.list_title.data,
        list_location = form.list_location.data,
        list_price = form.list_price.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.list_title.data = listing.list_title,
        form.list_location.data = listing.list_location,
        form.list_price.data = listing.list_price
    return render_template('update.html', title='Update Listing', form=form)


@app.route('/delete/<int:id>')
def delete(id):
    delete_listing = Listing.query.get(id)
    db.session.delete(delete_listing)
    db.session.commit()
    return redirect(url_for('index'))



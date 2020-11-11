from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Listing
from application.forms import ListingForm

app.route('/add', methods=['POST', 'GET'])
def add():
    form = ListingForm()
    if form.validate_on_submit():
        lister = Listing(
            title = form.title.data,
            list_description = form.list_description.data,
            categories = form.category.data
        )
        db.session.add(lister)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Create Listing", form=form)



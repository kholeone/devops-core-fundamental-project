from application import db
  
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable = false)
    categories = db.relationship('Category', backref='listing'i)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_description = db.Column(db.String(4000), nullable = false)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)

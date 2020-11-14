from application import db
  
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_title = db.Column(db.String(80), nullable = False)
    list_location = db.Column(db.String(80), nullable = False)
    list_price = db.Column(db.Float, nullable = False)
    listing = db.relationship('Detail', backref='listing')

class Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail_description = db.Column(db.String(4000), nullable = False)
    detail_category = db.Column(db.String(20), nullable = False)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)

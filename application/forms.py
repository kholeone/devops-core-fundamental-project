from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Listing, Category

class ListingForm(FlaskForm):
    title = StringField('Title',
            validators = [
                DataRequired(),
                ]
            )
    description = StringField('Description',
            validators = [
                DataRequired(),
                ]
            )
    categories = SelectField('All Categories',
            choices=[('antiques', 'Antiques'), ('art', 'Art'), ('baby', 'Baby'),
                ('books', 'Books, Comics & Magazines'), ('office', 'Business, Office & Industrial'),
                ('cameras', 'Cameras & Photography'), ('vehicles', 'Cars, Motorcycles & Vehicles'),
                ('clothes',' Clothes, Shoes & Accessories'),('coins', 'Coins'), ('computers', 'Computers/Tablets & Networking'),
                ('crafts', 'Crafts'), ('dolls', 'Dolls & Bears'), ('dvds', 'DVDs, Films & TV'), ('events', 'Events Tickets'),
                ('garden', 'Garden & Patio'), ('health', 'Health & Beauty'), ('holiday', 'Holidays & Travel'), ('home', 'Home, Furniture & DIY'),
                ('jewellery', 'Jewellery & Watches'),('mobile', 'Mobile Phones & Communication'), ('music', 'Music'), ('musicalinstruments', 'Musical Instruments'),
                ('pet', 'Pet Supplies'), ('pottery', 'Pottery, Porcelain & Glass'),('property', 'Property'), ('sound', 'Sound & Vision'), ('sporting', 'Sporting Goods'),
                ('sports', 'Sports Memorabilia'), ('stamps', 'Stamps'), ('toys', 'Toys & Games'),('vehicleparts', 'Vehicle Parts & Accessories'),
                ('videogames', 'Video Games & Console'), ('wholesale', 'Wholesale & Job Lots'), ('everythingelse', 'Everything Else')
                ]
            )
    submit = SubmitField('Post Listing')


"""Seed file to make sample data for adopt db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

pic1 = 'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/green-sea-turtle-1.jpg'
pic2 = 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-cat-photos-1593441022.jpg'

p1 = Pet(name='Alvin', species='Turtle', photo_url=pic1, age=47, notes='Very old', available=True)
p2 = Pet(name='Ben', species='Turtle', age=28, notes='Somewhat old', available=False)
p3 = Pet(name='Sarah', species='Turtle', notes='Very old', available=True)
p4 = Pet(name='Billy', species='Dog', notes='Billy is annoying', available=True)
p5 = Pet(name='Birb', species='Bird', notes='Birb is the word', available=False)
p6 = Pet(name='Fluffy', species='Cat', age=8, notes='Very old', available=False)
p7 = Pet(name='Jumpy', species='Cat', photo_url=pic2, age=13)
p8 = Pet(name='Angry', species='Bird', age=6)

db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
db.session.commit()
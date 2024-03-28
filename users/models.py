from mongoengine import Document, StringField, EmailField, BooleanField

# Create your models here.
class MongoUser(Document):
    username = StringField(required=True, min_length=3, max_length=50, unique=True)
    password = StringField(required=True, min_length=4, max_length=50)
    email = EmailField(required=True, unique=True, max_length=200)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)


    meta = {'collection': 'users'}

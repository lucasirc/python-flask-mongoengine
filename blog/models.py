import datetime
from mongoengine import *


class Post(Document):
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    title = StringField(max_length=255, required=True, min_length=1)

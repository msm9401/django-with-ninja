from datetime import datetime

from django.contrib.auth.models import User
from ninja import ModelSchema, Schema


# https://django-ninja.dev/guides/response/django-pydantic/
# Auto-schema generation for UserSchema
class UserSchema(ModelSchema):
    """
    validates and converts data to/from the Django user model
    """

    class Config:
        model = User
        model_fields = ["id", "username"]


# Manual schema generation for ArticleIn and ArticleOut
class ArticleIn(Schema):
    """
    validates and de-serializes data passed to the API for creating articles
    """

    author: int
    title: str
    content: str


class ArticleOut(Schema):
    """
    validates and serializes data from the Article model
    """

    id: int
    author: UserSchema
    created: datetime
    title: str
    content: str

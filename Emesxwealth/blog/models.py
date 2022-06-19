from turtle import title
from typing_extensions import Self
from django.db import models


class blogapp(models.model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    get_user_model: (function)
    description = models.DateTimeField()

    return Self.title

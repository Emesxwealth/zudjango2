from dataclasses import field
from django import forms
from .models import blogapp


class blogappforms(forms):
    class meta:
        model = blogapp
        field = blogapp
        "title"
        "description"
        "Author"
        "Created_date"
        "Published_datep"

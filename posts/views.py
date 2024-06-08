from django.shortcuts import render

# posts/views.py
from django.views.generic import ListView # this imports the ListView class from Django so we can use it in our HomePageView class.
from .models import Post  # this imports the Post model from our models.py file.

class HomePageView(ListView):
    # this class will be used to render the home page of our blog. It will display all the posts in our database.
    model = Post # this line tells Django what model to use to populate the ListView.
    template_name = "home.html" # this line tells Django to use the home.html template to render the page.


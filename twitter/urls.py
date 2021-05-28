from django.urls import path
from .views import TwitterShare, TwitterPost, TwitterGet, TwitterBackground
urlpatterns = [
    path("share/", TwitterShare, name="twitter-share"),
    path("post/", TwitterPost, name="twitter-post"),
    path("get/<int:pk>/", TwitterGet, name="twitter-get"),
    path("background/", TwitterBackground, name="twitter-background"),
]
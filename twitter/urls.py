from django.urls import path
from .views import TwitterShare, TwitterPost, TwitterGet
urlpatterns = [
    path("share/", TwitterShare, name="twitter-share"),
    path("post/", TwitterPost, name="twitter-post"),
    path("get/<int:pk>/", TwitterGet, name="twitter-get"),
]
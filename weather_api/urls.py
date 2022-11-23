from django.urls import path
from . import views
#  In this section, we enter the path of the functions that we defined in the views to communicate with the templates.
urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    # path('social_links', views.social_links),
]

from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('me/',UserView.as_view(),name="retrieve_user")
]
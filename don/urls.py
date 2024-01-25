# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.index, name="index")   
# ]
# from django.urls import path
# from .views import check_firebase_connection

# urlpatterns = [
#     # Your other URL patterns here

#     # Add a URL pattern for checking Firebase connection
#     path('', check_firebase_connection, name='check_firebase_connection'),
# ]

# urls.py
from django.urls import path
from .views import read_data_from_firebase

urlpatterns = [
    # Your other URL patterns here

    path('', read_data_from_firebase, name='read_data_from_firebase'),
]

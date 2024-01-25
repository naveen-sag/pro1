from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("your djago setup is ready")


# In your views.py
# from .firebase_cofig import cred

# print("Firebase Admin SDK initialized successfully!")  # Add this line

# from django.shortcuts import render
# from django.http import HttpResponse
# from .firebase_cofig import cred

# def check_firebase_connection(request):
#     # Print a message indicating Firebase Admin SDK initialization
#     print("Firebase Admin SDK initialized successfully!")

#     # You can also include additional checks or messages here

#     return HttpResponse("Firebase Admin SDK initialization check complete.")

# views.py
from django.http import JsonResponse
from firebase_admin import db
from .firebase_cofig import cred

def read_data_from_firebase(request):
    # Create a reference to the root node ('/')
    root_ref = db.reference('/')

    # Read data from Firebase
    data = root_ref.get()

    # Return the data as a JSON response
    return JsonResponse({'data_from_firebase': data})






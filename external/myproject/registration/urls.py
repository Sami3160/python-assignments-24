from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register_page,name="register"),
    # path('submit-registration/', views.handle_submit, name="submit_registration"),
]

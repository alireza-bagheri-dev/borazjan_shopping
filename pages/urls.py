from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.HomePageView.as_view(), name='home'),
]
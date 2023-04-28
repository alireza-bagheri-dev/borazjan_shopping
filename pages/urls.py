from django.urls import path

import products.views
from . import views

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home_page'),
    path('', products.views.ProductListView.as_view(), name='home'),
]

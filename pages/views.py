import django.views.generic
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'

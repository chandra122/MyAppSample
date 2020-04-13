from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name = 'blog-home'),
    path('about/',views.about, name = 'blog-about'),
    path('about1/',views.example, name = 'blog-about1'),
]
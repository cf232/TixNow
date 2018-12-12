from django.urls import path
from TixNow import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search)
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.chat_home, name = "home"),
    path('<str:room_name>/', views.room, name="room"),
]
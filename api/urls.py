
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.userLogin, name="userLogin"),
    path('logout', views.userLogout, name="userLogout")
]

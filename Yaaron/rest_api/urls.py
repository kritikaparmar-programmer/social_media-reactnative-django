from django.urls import path
from .views import HelloWorld

urlpatterns = [
    path('helloworld/', HelloWorld.as_view())
] 
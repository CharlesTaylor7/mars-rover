from django.urls import path
from . import views

urlpatterns = [
    path('<rover>/<camera>/', views.index, name='index'),
]

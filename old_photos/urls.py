from django.urls import path
from . import views

urlpatterns = [
    path('photos/<rover>/<camera>/', views.photos, name='photos'),
    path('cameras/', views.cameras, name='cameras'),
]

from django.urls import path

from . import views


urlpatterns = [
    path('<int:place_id>/', views.get_place, name='place_json'),
]

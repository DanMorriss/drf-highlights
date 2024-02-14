from django.urls import path
from location import views


urlpatterns = [
    path('locations/', views.LocationList.as_view()),
    path('locations/<int:pk>/', views.LocationDetail.as_view()),
]

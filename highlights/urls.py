from django.urls import path
from highlights import views


urlpatterns = [
    path('highlights/', views.HighlightList.as_view()),
    path('highlights/<int:pk>/', views.HighlightDetail.as_view()),
]

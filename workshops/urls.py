from django.urls import path
from workshops import views


urlpatterns = [
    path('workshops/', views.WorkshopList.as_view()),
    path('workshops/<int:pk>/', views.WorkshopDetail.as_view()),
]

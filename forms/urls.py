from django.urls import path
from forms import views

urlpatterns = [
    path('forms/', views.FormtDetail.as_view()),
]
from django.urls import path
from jobs import views

urlpatterns = [
    path('<int:job_id>/', views.jobdetails, name='jobdetails'),
]

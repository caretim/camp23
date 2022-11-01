from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
]

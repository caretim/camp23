from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/photos/", views.photos, name="photos"),
    path("<int:pk>/add-photo/", views.add_photo, name="add-photo"),
    path("<int:article_pk>/delete", views.delete, name="delete"),
]

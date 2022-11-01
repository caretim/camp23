from django.db import models
from Camp23.settings import AUTH_USER_MODEL
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Article(models.Model):
    image = models.ImageField(
        default="images/default_image.jpeg",
        upload_to="images/",
        blank=True,
    )
    thumbnail = ProcessedImageField(
        upload_to="thumbnail/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={
            "quality": 60,
        },
    )
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=14)
    camp_type = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    active_day = models.CharField(max_length=10)
    reservation = models.CharField(max_length=15)
    amenities = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SubImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    sub_image = models.ImageField(
        default="images/default_image.jpeg",
        upload_to="images/",
        blank=True,
    )


class Geography(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tags = models.CharField(max_length=10)

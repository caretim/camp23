from django.db import models
from reviews.models import Review
from articles.models import Article
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


def input_only_number(value):
    if not value.isdigit():
        raise ValidationError("숫자만 적을 수 있습니다.")


class User(AbstractUser):
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="follower"
    )
    marker = models.ManyToManyField(Article, related_name="articles")
    like_reviews = models.ManyToManyField(Review, related_name="like_it")
    phone = models.CharField(
        max_length=13,
        validators=[MinLengthValidator(11), MaxLengthValidator(11), input_only_number],
        blank=True,
    )

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"

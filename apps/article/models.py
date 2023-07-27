from ckeditor.fields import RichTextField
from django.db import models
from .choices import RecommendedChoices, StatusChoices, PositionChoices
from .managers import MainArticleManager, ArticleCategoryManager, ArticleRegionManager


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(
        choices=StatusChoices.choices, max_length=20, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(
        choices=StatusChoices.choices, max_length=20, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    images = models.ManyToManyField("Image")
    audio = models.FileField(upload_to="audio/", blank=True, null=True)
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag")
    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    position = models.CharField(
        max_length=10, choices=PositionChoices.choices, null=True, blank=True
    )
    recommended = models.CharField(max_length=5, choices=RecommendedChoices.choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    objects = MainArticleManager()
    category_manager = ArticleCategoryManager()
    region_manager = ArticleRegionManager()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.image.name


class ViewCount(models.Model):
    device_id = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

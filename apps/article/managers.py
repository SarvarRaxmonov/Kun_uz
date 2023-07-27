from django.db import models
from django.db.models import Q
from django.db.models import Max


class MainArticleManager(models.Manager):
    def get_latest_news(self):
        return (
            super()
            .get_queryset()
            .filter(status="published")
            .order_by("-created_at")[:8]
        )

    def get_prime_articles(self):
        return (
            super()
            .get_queryset()
            .filter(status="published", position="prime")
            .order_by("-created_at")[:5]
        )

    def get_prime_types_of_articles(self):
        return (
            super()
            .get_queryset()
            .filter(type__status="prime")
            .order_by("-created_at")[:3]
        )

    def get_urgent_articles(self):
        return (
            super()
            .get_queryset()
            .filter(type__status="prime", type__name="urgent")
            .order_by("-created_at")[:5]
        )

    def get_prime_interview_articles(self):
        return (
            super()
            .get_queryset()
            .filter(type__status="prime", type__name="interview")
            .order_by("-created_at")[:4]
        )

    def get_prime_themed_articles(self):
        return (
            super()
            .get_queryset()
            .filter(theme__status="prime")
            .order_by("-created_at")[:5]
        )

    def get_authored_articles(self):
        return (
            super()
            .get_queryset()
            .filter(type__status="prime", type__name="authored articles")
            .order_by("-created_at")[:6]
        )

    def get_advertisement_articles(self):
        return (
            super()
            .get_queryset()
            .filter(type__status="prime", type__name="advertisement")
            .order_by("-created_at")[:5]
        )

    def get_video_and_photo_articles(self):
        video = (
            super()
            .get_queryset()
            .filter(type__status="prime", type__name="video")
            .order_by("-created_at")[:3]
        )
        photo = (
            super()
            .get_queryset()
            .filter(type__status="prime", type__name="photo")
            .order_by("-created_at")[:3]
        )

        return [video, photo]

    def get_theme_articles(self, theme_name):
        return (
            super()
            .get_queryset()
            .filter(~Q(theme__exact=""), Q(theme_name=theme_name))
            .order_by("-created_at")
        )

    def get_typed_articles(self, type_name):
        return (
            super()
            .get_queryset()
            .filter(~Q(type__exact=""), Q(theme_name=type_name))
            .order_by("-created_at")
        )


class ArticleViewCountManager(models.Manager):
    def get_the_most_read_articles(self):
        return (
            super()
            .get_queryset()
            .values("article_id__id")
            .annotate(max_viewcount=Max("viewcount"))
            .order_by("article_id__created")[:5]
        )


class ArticleCategoryManager(models.Manager):
    def get_main_articles_by_category(self, category_name):
        return (
            super()
            .get_queryset()
            .filter(
                Q(category__name=category_name)
                and Q(type__status="prime") | Q(type__status="main")
            )
            .order_by("-created_at")[:5]
        )

    def get_category_articles(self, category_name):
        return (
            super()
            .get_queryset()
            .filter(category__name=category_name)
            .order_by("-created_at")
        )


class ArticleRegionManager(models.Manager):
    def get_main_articles_by_region(self, region_name):
        return (
            super()
            .get_queryset()
            .filter(
                Q(region__name=region_name)
                and Q(type__status="prime") | Q(type__status="main")
            )
            .order_by("-created_at")[:4]
        )

    def get_region_articles(self, region_name):
        return (
            super()
            .get_queryset()
            .filter(region__name=region_name)
            .order_by("-created_at")
        )

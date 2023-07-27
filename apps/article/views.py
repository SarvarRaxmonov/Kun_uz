from rest_framework import viewsets
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer


class MainViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        instance = Article.objects
        prime_positioned_articles = self.get_serializer(
            instance.get_prime_articles(), many=True
        )
        prime_type_of_articles = self.get_serializer(
            instance.get_prime_types_of_articles(), many=True
        )
        urgent_articles = self.get_serializer(instance.get_urgent_articles(), many=True)
        interview_articles = self.get_serializer(
            instance.get_prime_interview_articles(), many=True
        )
        themed_articles = self.get_serializer(
            instance.get_prime_themed_articles(), many=True
        )
        authored_articles = self.get_serializer(
            instance.get_authored_articles(), many=True
        )
        get_advertisement_articles = self.get_serializer(
            instance.get_advertisement_articles(), many=True
        )
        get_video_articles = self.get_serializer(
            instance.get_advertisement_articles(), many=True
        )
        get_photo_articles = self.get_serializer(
            instance.get_advertisement_articles(), many=True
        )
        latest_news = self.get_serializer(instance.get_latest_news(), many=True)

        return Response(
            {
                "prime_positioned_articles": prime_positioned_articles.data,
                "prime_type_of_articles": prime_type_of_articles.data,
                "urgent_articles": urgent_articles.data,
                "interview_articles": interview_articles.data,
                "themed_articles": themed_articles.data,
                "authored_articles": authored_articles.data,
                "get_advertisement_articles": get_advertisement_articles.data,
                "get_video_articles": get_video_articles.data,
                "get_photo_articles": get_photo_articles.data,
                "last_news": latest_news.data,
            }
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, name=None):
        instance = Article
        main_article = self.get_serializer(
            instance.category_manager.get_main_articles_by_category(name), many=True
        )
        articles = self.get_serializer(
            instance.category_manager.get_category_articles(name), many=True
        )
        latest_news = self.get_serializer(instance.objects.get_latest_news(), many=True)
        return Response(
            {
                "category_main_articles": main_article.data,
                "articles": articles.data,
                "latest_news": latest_news.data,
            }
        )


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, name=None):
        instance = Article
        main_article = self.get_serializer(
            instance.region_manager.get_main_articles_by_region(name), many=True
        )
        articles = self.get_serializer(
            instance.region_manager.get_region_articles(name), many=True
        )
        latest_news = self.get_serializer(instance.objects.get_latest_news(), many=True)
        return Response(
            {
                "region_main_articles": main_article.data,
                "articles": articles.data,
                "latest_news": latest_news.data,
            }
        )


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, name=None):
        instance = Article
        articles = self.get_serializer(
            instance.objects.get_theme_articles(name), many=True
        )
        the_most_readed = ""
        return Response(
            {
                "articles": articles.data,
                "latest_news": latest_news.data,
            }
        )

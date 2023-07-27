from rest_framework import routers
from django.urls import path
from .views import MainViewSet, CategoryViewSet, RegionViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("main_page", MainViewSet.as_view({"get": "list"}), name="main_page"),
    path(
        "category/<str:name>",
        CategoryViewSet.as_view({"get": "retrieve"}),
        name="category",
    ),
    path(
        "region/<str:name>", RegionViewSet.as_view({"get": "retrieve"}), name="region"
    ),
]

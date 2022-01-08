from django.urls import path
from .views import book, category

urlpatterns = [
    path('book/nested-serializer/', book),
    path('category/nested-serializer/', category )
]
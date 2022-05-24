from django.urls import path
from .views import BookViewSet, JournalViewSet, UserCreateList, login, logout
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'journals', JournalViewSet, basename='journal')

urlpatterns = [
    path('register/', UserCreateList.as_view()),
    path('login/', login),
    path('logout/', logout)
] + router.urls
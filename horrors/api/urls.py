from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ReviewView, expired_obtain_auth_token


router = SimpleRouter()
router.register(r'posts', ReviewView)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', expired_obtain_auth_token)
]
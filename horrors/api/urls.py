from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import expired_obtain_auth_token
#, ReviewView
#
#
# router = SimpleRouter()
# router.register(r'posts'
#                 #, ReviewView
#                 )


urlpatterns = [
    # path('', include(router.urls)),
    path('auth/', expired_obtain_auth_token)
]
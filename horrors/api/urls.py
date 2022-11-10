from django.urls import path

from .views import expired_obtain_auth_token

urlpatterns =[
    path('auth/', expired_obtain_auth_token, name='api-auth')
]
from django.urls import path
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from users.api import UserCreateAPIView
from users.serializers import UserPublicSerializer

urlpatterns = [
    path(
        "",
        swagger_auto_schema(
            method="post",
            responses={
                201: openapi.Response("response description", UserPublicSerializer)
            },
        )(UserCreateAPIView.as_view()),
    ),
]

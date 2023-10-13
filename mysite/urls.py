from django.urls import include, path

urlpatterns = [
    path("spam/", include("spam.urls"))
]

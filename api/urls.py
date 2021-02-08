from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Users', views.UsersView, basename="Users")
router.register('Fotos', views.FotosView, basename="Fotos")


urlpatterns = [
    path('', include(router.urls)),
]

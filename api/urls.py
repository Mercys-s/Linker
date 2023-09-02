from django.urls import path , include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import WorkflowViewSet


router = DefaultRouter ()
router.register ('' , viewset = WorkflowViewSet)


urlpatterns = [
    path ('workflow/' , include (router.urls)),
    path ('auth/', view = views.obtain_auth_token),
]
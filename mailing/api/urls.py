from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, MailingViewSet, MessageViewSet

router = DefaultRouter()
router.register('client', ClientViewSet)
router.register('mailing', MailingViewSet)
router.register('message', MessageViewSet)
urlpatterns = [
    path('v1/', include(router.urls)),
]

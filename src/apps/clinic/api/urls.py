from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views


router = DefaultRouter()
router.register(r'certificates', views.CertificateViewSet, 'certificate')
router.register(r'specialists', views.SpecialistViewSet, 'specialist')
router.register(r'media', views.MediaViewSet, 'media')

urlpatterns = (
    path('', include(router.urls)),
    path('config/', views.ClinicConfigAV.as_view())
)

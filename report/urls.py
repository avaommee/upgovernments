from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('register', views.admin, name='register'),
                  path('safe', views.safe, name='save'),
                  path('fetch', views.fetch, name='fetch'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

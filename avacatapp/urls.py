from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'avacatapp'
urlpatterns = [
    url(r'^$', views.index, name='index')
]

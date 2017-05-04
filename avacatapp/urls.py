from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import newResourceView

app_name = 'avacatapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^resource/new/$',
        newResourceView.as_view(),
        name='new-resource',
    ),
]

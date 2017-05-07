from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'avacatapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^new$',views.ResourceCreate.as_view(),name='resource_new',),
    url(r'^edit/(?P<pk>\d+)$', views.ResourceUpdate.as_view(), name='resource_edit'),
    url(r'^like/(?P<id>\d+)$', view=views.like, name ='like_resourse'),
    url(r'^dislike/(?P<id>\d+)$', view=views.dislike, name ='dislike_resourse')

]

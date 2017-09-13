from django.shortcuts import render
from .search import *
from django.views.generic import CreateView, UpdateView
from .models import Resource, Like
from .forms import ResourceForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import TrigramSimilarity
from django.urls import reverse
from datetime import datetime

@login_required
def index(request):
    searchTerm = request.GET.get('q', '')
    context = {'searchTerm': searchTerm}
    return render(request, 'index.html', context)

@csrf_exempt
def search(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    searchTerm = body['searchTerm']
    page = body['page']

    resources = list(Resource.objects.annotate(
             similarity=TrigramSimilarity( 'name', searchTerm)
             )
             .filter(similarity__gt=0.05).order_by('-similarity'))

    for r in resources:
        r.view_count += 1
        r.last_viewed_date = datetime.now()
        r.save()
        r.image = r.image.url
        r.value = r.value.replace('\n', '<br/>')
        r.likes = Like.objects.filter(resource_id = r.pk).count()
        r.is_liked_by_user = Like.objects.filter(user_id = request.user.id, resource_id = r.pk ).count() > 0

    resources.sort(key=lambda x: [-x.likes, -x.view_count] )
    paginator = Paginator(resources, 10)
    paged_resources = paginator.page(page)
    data = serializers.serialize('json', paged_resources)
    return HttpResponse(data, content_type='application/json')

def like(request, id):
    resource = Resource.objects.get(pk=id)
    try:
        likeObject = Like.objects.get(user_id = request.user.id, resource_id = id )
    except Exception as e:
         likeObject = None
         print(str(e))
    if likeObject == None:
        Like.create(request.user, resource)
    else:
        Like.remove(request.user, resource)

    number_of_likes = Like.objects.filter(resource=resource).count()
    return HttpResponse(number_of_likes)

class ResourceCreate(CreateView):
    model = Resource
    template_name  ="avacatapp/new_resource_form.html"
    fields = ['name', 'value', 'link', 'image']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.last_modified_by = self.request.user
        object.save()
        return super(ResourceCreate, self).form_valid(form)
    def get_success_url(self):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.full_clean()
        return "/?q=" + form.cleaned_data['name']

class ResourceUpdate(UpdateView):
    model = Resource
    template_name = "avacatapp/edit_resource_form.html"
    success_url = "/"
    fields = ['name', 'value', 'link', 'image']

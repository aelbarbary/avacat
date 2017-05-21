from django.shortcuts import render
from .search import *
from django.views.generic import CreateView, UpdateView
from .models import Resource
from .forms import ResourceForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
import json
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    searchTerm = request.GET.get('q', '')
    print(searchTerm)
    context = {'searchTerm': searchTerm}
    return render(request, 'index.html', context)

@csrf_exempt
def search(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    searchTerm = body['searchTerm']
    resources = list(Resource.objects.filter(name__icontains = searchTerm)
                    .order_by('-likes', 'dislikes') )
    for resource in resources:
        resource.image = resource.image.url
        resource.value = resource.value.replace('\n', '<br/>')
    data = serializers.serialize('json', resources)
    return HttpResponse(data, content_type='application/json')

def like(request, id):
    print(id)
    obj = Resource.objects.get(pk=id)
    obj.likes = obj.likes + 1;
    obj.save()
    return HttpResponse()

def dislike(request, id):
    print(id)
    obj = Resource.objects.get(pk=id)
    obj.dislikes = obj.dislikes + 1;
    obj.save()
    return HttpResponse()

class ResourceCreate(CreateView):
    model = Resource
    template_name  ="avacatapp/new_resource_form.html"
    success_url = "/"
    fields = ['name', 'value', 'link', 'image']

class ResourceUpdate(UpdateView):
    model = Resource
    template_name = "avacatapp/edit_resource_form.html"
    success_url = "/"
    fields = ['name', 'value', 'link', 'image']

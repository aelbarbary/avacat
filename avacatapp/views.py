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


def index(request):
    context = {}
    return render(request, 'index.html', context)

@csrf_exempt
def search(request):
    print (request.POST.get('searchTerm'))
    searchTerm = request.POST.get('searchTerm')
    resources = list(Resource.objects.filter(name__icontains = searchTerm)
                    .order_by('-likes', 'dislikes') )
    for resource in resources:
        resource.image = resource.image.url
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
    success_url = "/"
    fields = ['name', 'description', 'link', 'image']

class ResourceUpdate(UpdateView):
    model = Resource
    success_url = "/"
    fields = ['name', 'description', 'link', 'image']

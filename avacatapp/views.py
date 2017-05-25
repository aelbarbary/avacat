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
    resources = list(Resource.objects.filter(name__icontains = searchTerm))
    for r in resources:
        r.image = r.image.url
        r.value = r.value.replace('\n', '<br/>')
        r.likes = Like.objects.filter(resource_id = r.pk).count()
        r.is_liked_by_user = Like.objects.filter(user_id = request.user.id, resource_id = r.pk ).count() > 0
    data = serializers.serialize('json', resources)
    return HttpResponse(data, content_type='application/json')

def like(request, id):
    resource = Resource.objects.get(pk=id)
    try:
        likeObject = Like.objects.get(user_id = request.user.id, resource_id = id )
    except Exception as e:
         likeObject = None
         print(str(e))
    if likeObject == None:
        print("adding");
        Like.create(request.user, resource)
    else:
        print("removing")
        Like.remove(request.user, resource)

    number_of_likes = Like.objects.filter(resource=resource).count()
    print("number_of_likes:" + str(number_of_likes))
    return HttpResponse(number_of_likes)

class ResourceCreate(CreateView):
    model = Resource
    template_name  ="avacatapp/new_resource_form.html"
    success_url = "/"
    fields = ['name', 'value', 'link', 'image']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.last_modified_by = self.request.user
        object.save()
        return super(ResourceCreate, self).form_valid(form)

class ResourceUpdate(UpdateView):
    model = Resource
    template_name = "avacatapp/edit_resource_form.html"
    success_url = "/"
    fields = ['name', 'value', 'link', 'image']

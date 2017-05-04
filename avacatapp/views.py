from django.shortcuts import render
from .search import *
from django.views.generic import CreateView
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
    searchTerm = request.POST.get('searchTerm')
    resources = list(Resource.objects.filter(name__icontains = searchTerm))
    data = serializers.serialize('json', resources)
    return HttpResponse(data, content_type='application/json')

class newResourceView(CreateView):
    template_name = 'new_resource_form.html'
    model = Resource
    form_class = ResourceForm
    success_url = "/"

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form))
    def post(self, request, *args, **kwargs):
        print(request)
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if (form.is_valid()):
            print("valid")
            return self.form_valid(form)
        else:
            print("invalid")
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))

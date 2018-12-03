from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (ListView, CreateView, DetailView, DeleteView)
from rest_framework.parsers import JSONParser

from .forms import FormProject
from .models import Project
from .serializers import ProjectSerializers


@csrf_exempt
def _list(request):
    if request.method == "GET":  # list
        projects = Project.objects.all()
        serializer = ProjectSerializers(projects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":  # create
        data = JSONParser().parse(request)
        serializer = ProjectSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return HttpResponse(status=404)


@csrf_exempt
def _detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":  # detail
        serializer = ProjectSerializers(project)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":  # update
        data = JSONParser().parse(request)
        serializer = ProjectSerializers(project, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":  # delete
        project.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=404)


class _ListProject(ListView):
    template_name = "project/list.html"
    model = Project
    context_object_name = "projects"


class _CreateProject(CreateView):
    template_name = "project/create.html"
    model = Project
    form_class = FormProject
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class _DetailProject(DetailView):
    template_name = "project/detail.html"
    model = Project
    context_object_name = "project"


class _DeleteProject(DeleteView):
    template_name = "project/delete.html"
    model = Project
    context_object_name = "project"
    success_url = "/"

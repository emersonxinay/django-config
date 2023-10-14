from django.http import HttpResponse, JsonResponse
from blog.models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def  index(request):
  projects = list(Project.objects.values())
  
  return JsonResponse(projects, safe= False)

def  hola(request, usuario):

  return HttpResponse("<h1>Hola mundo %s </h1>" % usuario)

def nosotros(request):
  
  title = 'Django Course!!'
  return render(request, 'index.html', { 'title': title })
  

def taks(request, id):
  task = get_object_or_404(Task, id=id)
  
  return HttpResponse('task: %s' %task.title)
from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=200)
  # para mostrar los datos a una consulta
  def __str__(self):
    return self.name
  
  
class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  # la relacion con la tabla project 
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  def __str__(self):
    return self.title + '-' + self.project.name
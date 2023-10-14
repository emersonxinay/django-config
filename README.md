# Iniciar con Django 

## verificar la versión de Python 
```bash
python --version
```
## para crear la carpeta del entorno virtual
```bash
pytho3 -m venv venv
```
## para activar el entorno virtual
en MAC
```bash
source venv/bin/activate
```
en WINDOWS
```bash
venv/Scripts/activate
```

## Instalar Django
```bash
pip install Django
```
## crear proyecto con Django 
```bash
django-admin startproject mysitio .
```
## ejecutar proyecto 
```bash
python manage.py runserver
```
## ejecutar proyecto con puerto especifico 
```bash
python manage.py runserver 3000
```

# Para verficar todas opciones que se pueda hacer 

```bash
python manage.py --help
```
## para crear nuevas aplicaciones dentro del proyecto 
```bash
python manage.py startapp nombreapp
```
# crear base de datos 
## iniciar creación de base de datos
```bash
python manage.py makemigrations
```
## para hacer migracion
```bash
python manage.py migrate
```

## desde el archivo blog/models.py creamos los modelos para las base de datos
```python
# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=200)
```
## para conectar la carpeta blog con la carpeta principal del proyecto
```python
# misitio1/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', # agregado
]
```
## previas a migrar a carpeta especifica 
```bash
python manage.py makemigrations blog
```
## para hacer migracion a carpeta especifica
```bash
python manage.py migrate blog
```

## para crear relacion entre tablas
```python
# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=200)
  
  
class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  # la relacion con la tabla project 
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
```
### nuevamente migramos y corremos 
## previas a migrar a carpeta especifica 
```bash
python manage.py makemigrations blog
```
## para hacer migracion a carpeta especifica
```bash
python manage.py migrate blog
```

## para ingresar a DJANGO SHELL
```bash
python manage.py shell
```
## dentro de shell agregamos datos a la bd
Para importar todo
```bash
from blog.models import Project, Task

```
Para crear un dato 
```bash
 p = Project(name= "mis app")
```
Para guardar 
```bash
p.save()
```
Para ver todos los objetos creados
```bash
Project.objects.all()
```
Para buscarlo por id
```bash
Project.objects.get(id=1)
```
Para buscarlo por nombre
```bash
Project.objects.get(name="mis apps")
```
## para crear con claves foraneas las tablas
guardamos en una variable una petición
```bash
p= Projects.objects.get(id=1)
```
verificar que todo este okey el query
```bash
p.task_set.all()
```
para crear un nuevo dato en tarea de acuerdo aa los atributos del modelo 
```bash
p.task_set.create(title="descargar")
```
para buscar con que nombre inicia
```bash
Project.objects.filter(name__startswith="mis")
```
# panel de administrador django 
por defecto esta en al ruta raiz /admin
para ingresar a la consola de super admin
```bash
python manage.py createsuperuser
```
y crearse su usuarios:
```text
usuario: emerson
password: 123456
email: emer@gmail.com
```
## para agregar nuestros modelos en el panel admin
```py
# blog/admin.py
from .models import Project, Task
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
```

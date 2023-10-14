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
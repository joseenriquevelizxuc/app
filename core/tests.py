from app.wsgi import *
from core.models import *

# LISTAR

print(Category.objects.all())

for i in Category.objects.filter():
    print(i)
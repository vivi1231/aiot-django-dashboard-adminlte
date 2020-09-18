
from datetime import date
from app.models import PERSON, FACE


PERSON.objects.create(in_out=True)
FACE.objects.create(age=0, gender=False)


python manage.py shell

from datetime import date
from app.models import PERSON, FACE


PERSON.objects.create(in_out=True)

python manage.py shell
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","recall_five.settings")

import django
django.setup()

from faker import Faker
from first_recall.models import Teacher
fakergen=Faker()

def populate(N=5):
    for i in range(N):
        faker_name=fakergen.name()
        faker_email=fakergen.email()
        faker_mobile=fakergen.phone_number()

        teacher=Teacher.objects.get_or_create(Name=faker_name,Email=faker_email,Mobile=faker_mobile)

if __name__=='__main__':
    print("starting populate")
    populate(10)
    print("teacher populated successfully")

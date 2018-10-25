from random import choice
from transfergoating.celery import app
from .utils import herder_create
from .models import *


@app.task
def farmer_arrive():
    herder_create()


@app.task
def transfer_goats():
    disactive_herders = Herder.objects.filter(is_active=False)

    for herder in disactive_herders:
        herder.is_active = True
        herder.save()

    herder = choice(Herder.objects.all())

    farm = Farm.objects.first()
    farm.herder = herder
    farm.save()

    goats = Goat.objects.all()

    for goat in goats:
        goat.herder = herder
        goat.save()

import random
from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import Kviz, Osoba, Pitanja, Odgovori
from main.factory import KvizFactory, OsobaFactory, PitanjaFactory, OdgovoriFactory

NUM_KVIZ = 10
NUM_OSOBA = 10
NUM_PITANJA = 1000
NUM_ODGOVORI = 1000

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Kviz, Osoba, Pitanja, Odgovori]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_KVIZ):
            kviz = KvizFactory()

        for _ in range(NUM_OSOBA):
            osoba = OsobaFactory()

        for _ in range(NUM_PITANJA):
            pitanje = PitanjaFactory(naziv="Primjer pitanja")
        for _ in range(NUM_ODGOVORI):
            odgovori = OdgovoriFactory()
            
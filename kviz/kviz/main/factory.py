import factory
from factory.django import DjangoModelFactory
import random

from main.models import *

class KvizFactory(DjangoModelFactory):
    class Meta:
        model = Kviz

    imeKviza = factory.Faker("first_name")
    tezina = factory.LazyAttribute(lambda x: random.randrange(0, 1000))
    kategorija = factory.Faker("sentence", nb_words=4)
    

class OsobaFactory(DjangoModelFactory):
    class Meta:
        model = Osoba

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    pitanjeOdg2 = factory.LazyAttribute(lambda x: random.randrange(0, 10))
    PrijavljenaZaKviz = factory.Iterator(Kviz.objects.all())


class PitanjaFactory(DjangoModelFactory):
    class Meta:
        model = Pitanja

    naziv = factory.Faker("sentence", nb_words=3)
    kategorija = factory.Faker("sentence", nb_words=4)
    imeKviza = factory.Iterator(Kviz.objects.all())
    

class OdgovoriFactory(DjangoModelFactory):
    class Meta:
        model = Odgovori

    naziv = factory.Faker("sentence", nb_words=3)
    tocan_odg = factory.LazyFunction(lambda: random.choice([False, True]))
    text = factory.Faker("sentence", nb_words=10)
    
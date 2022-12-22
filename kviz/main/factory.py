import factory
from factory.django import DjangoModelFactory
import factory.fuzzy

from main.models import *

class KvizFactory(DjangoModelFactory):
    class Meta:
        model = Kviz

    imeKviza = factory.Faker("first_name")
    tezina = factory.fuzzy.FuzzyInteger(0, 1000)
    kategorija = factory.Faker("sentence", nb_words=4)
    

class OsobaFactory(DjangoModelFactory):
    class Meta:
        model = Osoba

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    pitanjeOdg2 = factory.fuzzy.FuzzyInteger(0, 10)
    PrijavljenaZaKviz = factory.SubFactory(KvizFactory)


class OdgovoriFactory(DjangoModelFactory):
    class Meta:
        model = Odgovori

    naziv = factory.Faker("sentence", nb_words=4)
    text = factory.Faker("sentence", nb_words=50)
    tocan_odg = factory.Faker("boolean")


class PitanjaFactory(DjangoModelFactory):
    class Meta:
        model = Pitanja

    naziv = factory.Faker("sentence", nb_words=2)
    kategorija = factory.Faker("sentence", nb_words=5)
    text = factory.SubFactory(OdgovoriFactory)
    imeKviza = factory.SubFactory(KvizFactory)

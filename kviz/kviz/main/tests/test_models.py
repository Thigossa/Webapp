from django.test import TestCase
from main.models import *

class Testmodels(TestCase):

    def setUp(self):
        self.kviz1 = Kviz.objects.create(
            imeKviza='Geografija',
            tezina=1,
            kategorija='Znanje'
        )
        self.osoba1 = Osoba.objects.create(
            ime='Marko',
            prezime='Markić',
            pitanjeOdg2 = 1,
            PrijavljenaZaKviz = self.kviz1
        )
        self.odgovor1 = Odgovori.objects.create(
            naziv="Odgovor 1",
            text="Odgovor 1 text",
            tocan_odg=True
        )
        self.pitanje1 = Pitanja.objects.create(
            naziv="Pitanje 1",
            kategorija="Test",
            imeKviza=self.kviz1
        )
        self.pitanje1.text.add(self.odgovor1)
        

    def test_kviz_ime_kviza(self):
        self.assertEquals(self.kviz1.imeKviza, 'Geografija')

    def test_osoba_ime(self):
        self.assertEquals(self.osoba1.ime, 'Marko')
        
    def test_odgovori(self):
        self.assertEqual(self.odgovor1.naziv, "Odgovor 1")
        self.assertEqual(self.odgovor1.text, "Odgovor 1 text")
        self.assertEqual(self.odgovor1.tocan_odg, True)

    def test_pitanja(self):
        self.assertEqual(self.pitanje1.naziv, "Pitanje 1")
        self.assertEqual(self.pitanje1.kategorija, "Test")
        self.assertEqual(self.pitanje1.imeKviza, self.kviz1)
        self.assertEqual(self.pitanje1.text.first(), self.odgovor1)
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('main:index')

        self.assertEquals(resolve(url).func, index)

    def test_kviz_url_is_resolved(self):
        url = reverse('main:kviz')
        self.assertEquals(resolve(url).func.view_class, KvizList)

    def test_osoba_url_is_resolved(self):
        url = reverse('main:osoba')
        self.assertEquals(resolve(url).func.view_class, OsobaList)

    def test_pitanja_url_is_resolved(self):
        url = reverse('main:pitanja')
        self.assertEquals(resolve(url).func.view_class, PitanjaList)

    def test_odgovori_url_is_resolved(self):
        url = reverse('main:odgovori')

        self.assertEquals(resolve(url).func.view_class, OdgovoriList)
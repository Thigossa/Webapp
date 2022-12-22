from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('')

        self.assertEquals(resolve(url).func, index)

    def test_kviz_url_is_resolved(self):
        url = reverse('kviz')

        self.assertEquals(resolve(url).func.view_class, KvizList)

    def test_osoba_url_is_resolved(self):
        url = reverse('osoba')

        self.assertEquals(resolve(url).func.view_class, OsobaList)

    def test_osoba_url_is_resolved(self):
        url = reverse('pitanje')

        self.assertEquals(resolve(url).func.view_class, PitanjaList)

    def test_osoba_url_is_resolved(self):
        url = reverse('odgovori')

        self.assertEquals(resolve(url).func.view_class, OdgovoriList)
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('main:index')

    def test_project_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_kviz_GET(self):
        kviz_url = reverse('main:kviz')
        response = self.client.get(kviz_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kviz_list.html')

    def test_osoba_GET(self):
        osoba_url = reverse('main:osoba')
        response = self.client.get(osoba_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/osoba_list.html')

    def test_odgovori_GET(self):
        odgovori_url = reverse('main:odgovori')
        response = self.client.get(odgovori_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/odgovori_list.html')

    def test_pitanja_GET(self):
        pitanja_url = reverse('main:pitanja')
        response = self.client.get(pitanja_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/pitanja_list.html')

    
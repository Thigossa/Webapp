from django.db import models


class Kviz(models.Model):
    imeKviza = models.CharField(max_length=100)
    tezina = models.IntegerField()
    kategorija = models.CharField(max_length=50)
    def __str__(self):
        return self.imeKviza

class Osoba(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20)
    pitanjeOdg2 = models.IntegerField()
    PrijavljenaZaKviz = models.OneToOneField(Kviz,default=1,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.ime + " "+ self.prezime
    
class Odgovori(models.Model):
    naziv = models.CharField(max_length=100)
    text = models.TextField()
    tocanOdg = models.BooleanField()

class Pitanja(models.Model):
    naziv = models.CharField(max_length=100)
    kategorija = models.CharField(max_length=100)
    text = models.ManyToManyField(Odgovori)
    imeKviza = models.ForeignKey(Kviz, default=1, on_delete=models.CASCADE)

from django.db import models


class Kviz(models.Model):
    imeKviza = models.CharField(max_length=100)
    tezina = models.IntegerField(default=0) 
    kategorija = models.CharField(max_length=50)
    def __str__(self):
        return self.imeKviza

class Osoba(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    pitanjeOdg2 = models.IntegerField()
    PrijavljenaZaKviz = models.OneToOneField(Kviz,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.ime + " " + self.prezime

class Kandidat(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    godine = models.IntegerField()
    def __str__(self):
        return self.ime + " " + self.prezime

class Odgovori(models.Model):
    naziv = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    tocan_odg = models.BooleanField()
    def __str__(self):
        return self.naziv

class Pitanja(models.Model):
    naziv = models.CharField(max_length=100)
    kategorija = models.CharField(max_length=100)
    text = models.ManyToManyField(Odgovori)
    imeKviza = models.ForeignKey(Kviz, default=1, on_delete=models.CASCADE)
    def __str__(self):
        return self.naziv

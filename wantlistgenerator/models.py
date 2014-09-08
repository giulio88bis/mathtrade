from django.db import models


class Utente(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Libro(models.Model):

    ISBN = models.CharField(max_length=13)
    titolo = models.CharField(max_length=200)
    data_inserimento = models.DateTimeField()

    proprietario = models.ForeignKey(Utente)
    # foreignkey perché un utente può avere tanti libri
    # ma ogni libro ha un solo proprietario

    scambiabile_con = models.ManyToManyField(
        "self", symmetrical=False, blank=True)
    # manytomany perché il libro posso decidere di scambiarlo
    # con vari altri (sempre libri, quindi uso "self"),
    # ma symmetrical = false perché in generale
    # non so se gli altri vogliono scambiarlo con me
    # blank=True così non è necessario specificare all'inizio
    # con cosa voglio scambiarlo

    def __str__(self):
        return self.titolo

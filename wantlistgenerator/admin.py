from django.contrib import admin
from wantlistgenerator.models import Utente, Libro


class LibriDellUtente(admin.TabularInline):
    model = Libro  # faccio comparire i libri nella schermata della
                   # creazione utente direttamente
    extra = 0


class UtenteAdmin(admin.ModelAdmin):
    inlines = [LibriDellUtente]


admin.site.register(Utente, UtenteAdmin)

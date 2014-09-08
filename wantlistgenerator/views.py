from django.shortcuts import render
#from django.http import HttpResponse
from wantlistgenerator.models import Utente


def riassunto(request):
    utenti = Utente.objects.all()
    return render(request,
                  'wantlistgenerator/riassunto.html',
                  {'utenti': utenti}
                  )

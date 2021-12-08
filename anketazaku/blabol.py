from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    '''
    Tohle je priklad dvoudimenzionalniho pole, kde pevni sloupec je jmeno a ve druhem sloupci je dalsi pole znamek
    '''
    pole = [['Petr',[1,4,5,4]],['Pavel',[1,2,3,4,5]],['Maros',[1,2,2,1,3]],['Bohunka',[1,2,1,1,3]]]
    htmlOutput = "<HTML>"
    htmlOutput += "<body>"
    htmlOutput += "<H1>Toto je neco jineho</H1>"
    s = request.get_host()
    for x in request.GET:
        htmlOutput += x+"="+str(request.GET[x])+"<BR>"
    print( s)
    htmlOutput += "<BR>"
    htmlOutput += "</body>"
    htmlOutput += "</HTML>"
    return HttpResponse(htmlOutput)

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    '''
    Tohle je priklad  ankety
    '''
    pole = [['Otazka 1',[1,2,3,4]],['Otazka 2',[1,2,3,4,5]],['Otazka 3',[1,2,3,4,5]],['Otazka 4',[1,2,3,4,5]]]
    htmlOutput = "<HTML>"
    htmlOutput += "<body>"
    htmlOutput += "<H1>Anketa studenstva</H1>\n \
                    <FORM method='GET' action='blabol'>\n "
    ot=0
    for n in pole: 
        soucet = 0
        ot += 1
        pocet = 0
        htmlOutput += "<li>"+n[0]+" - má "+str(pocet)+" známek s průměrem :</li>"
        for z in n[1]:
            soucet+=z
            pocet+=1
            htmlOutput += "<input type=\"radio\" name=\"ot"+str(ot)+"\" value=\""+str(z)+"\">"+str(z)+"<BR>\n" 
    htmlOutput += " <BR>\n\
                    <input type='submit' value='Odesli'>\
                    </FORM>"
    htmlOutput += "</body>"
    htmlOutput += "</HTML>"
    return HttpResponse(htmlOutput)

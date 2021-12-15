from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from anketazaku.models import Answers, Question


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
    qs=Question.objects.all()

    for q in qs:
        htmlOutput += str(q.question_text)+"<BR>"
        xs=Answers.objects.filter(question=q.id)
        for z in xs:
            htmlOutput += "<input type=\"radio\" name=\"ot_"+str(q.question_text)+"\" value=\""+str(z.points)+"\">"+str(z.answer_text)+"<BR>\n"
#            htmlOutput += "<input type=\"radio\" name=\"ot"+str(ot)+"\" value=\""+str(z)+"\">"+str(z)+"<BR>\n" 
           
    htmlOutput += " <BR>\n\
                    <input type='submit' value='Odesli'>\
                    </FORM>"
                    
    htmlOutput += "</body>"
    htmlOutput += "</HTML>"
    return HttpResponse(htmlOutput)

def tmp(request):
    latest_question_list=Question.objects.all()
    template = loader.get_template('anketazaku/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def list(request):
    htmlOutput = "<HTML>"
    htmlOutput += "<body>"

    qs=Question.objects.all()
    
    for q in qs:
        htmlOutput += str(q.question_text)

    htmlOutput += "</body>"
    htmlOutput += "</HTML>"
    return HttpResponse(htmlOutput)

def detail(request, question_id):
    htmlOutput = "<HTML>"
    htmlOutput += "<body>"

    qs=Question.objects.get(id=question_id)

#    for q in qs:
#        htmlOutput += str(q[1].id)
    

    htmlOutput += str(qs.question_text)

    htmlOutput += "</body>"
    htmlOutput += "</HTML>"
    return HttpResponse(htmlOutput)


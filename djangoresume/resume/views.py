from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormData, FormEducation, FormLanguage, FormSkill, FormTech, FormTemplate, FormWork
from .models import Data, Skill, Education, Work, Language, Tech
from io import BytesIO
from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



def home_view(request):
    return render(request, "home.html", {})

def get_data(request):
    if request.method == 'POST':
        form = FormData(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tech')
    else:
        form = FormData()

    return render(request, 'profile.html', {'form': form})


def get_tech(request):
    if request.method == 'POST':
        form = FormTech(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skills')
    else:
        form = FormTech()

    return render(request, 'profile.html', {'form': form})

def get_skills(request):
    if request.method == 'POST':
        form = FormSkill(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/work')

    else:
        form = FormSkill()

    return render(request, 'skills.html', {'form': form})

def get_work(request):
    if request.method == 'POST':
        form = FormWork(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/education')

    else:
        form = FormWork()

    return render(request, 'work.html', {'form': form})

def get_education(request):
    if request.method == 'POST':
        form = FormEducation(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/language')

    else:
        form = FormEducation()

    return render(request, 'education.html', {'form': form})

def get_language(request):
    if request.method == 'POST':
        form = FormLanguage(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/template')

    else:
        form = FormLanguage()

    return render(request, 'language.html', {'form': form})

def get_template(request):
    if request.method == 'POST':
        form = FormTemplate(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/template1')

    else:
        form = FormTemplate()

    return render(request, 'template.html', {'form': form})

def template1_view(request):
    data = Data.objects.last()
    tech = Tech.objects.last()
    skill = Skill.objects.last()
    education = Education.objects.last()
    work = Work.objects.last()
    language = Language.objects.last()
    return render(request, "template1.html", {'data': data, 'tech': tech, 'skill': skill, 'education': education, 'work': work, 'language': language})

data = Data.objects.last()
tech = Tech.objects.last()
skill = Skill.objects.last()
education = Education.objects.last()
work = Work.objects.last()
language = Language.objects.last()
datas = {'data': data, 'tech': tech, 'skill': skill, 'education': education, 'work': work, 'language': language}

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('template1.html', datas)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response


    


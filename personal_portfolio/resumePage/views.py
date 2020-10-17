from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

from .models import Resume
from django.views.decorators.clickjacking import xframe_options_exempt


def resume(request):
    pdfs = Resume.objects.all()
    return render(request, 'resumePage/resume.html', {'pdfs': pdfs})


def pdf(request):
    return render(request, 'resumePage/pdf.html')

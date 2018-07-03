from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import TestResult, BrowserReport
# Create your views here.

class ResultsView(generic.ListView):
    template_name = 'run_results/index.html'
    def get_queryset(self):
        return TestResult.objects.order_by('-run_date')

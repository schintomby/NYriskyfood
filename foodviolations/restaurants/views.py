# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from restaurants.models import Violation
# Create your views here.

def index(request):
    violations = Violation.objects.filter(num_uncorrected_critical_violations__gt = 0).order_by('facility__county')
    context = {
        'violations': violations
    }
    return render(request, 'index.html', context)
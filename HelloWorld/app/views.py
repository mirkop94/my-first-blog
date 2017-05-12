# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
  html = "<html><body><p>Hello, world!</p></body></html>"
  return HttpResponse(html)
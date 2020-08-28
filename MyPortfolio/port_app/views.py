from django.shortcuts import render

from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from . import models
from django.views import generic
from django.core.urlresolvers import reverse
# Create your views here.

class ListProjects(generic.ListView):
    model = Projects

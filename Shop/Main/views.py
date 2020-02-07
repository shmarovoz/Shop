from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import *


class CategoryList(ListView):
    model = Category
    queryset = Category.objects.filter(categories=None)
    context_object_name = 'categories'
    template_name = 'Main/CategoryList.html'


class SubCategoryList(DetailView):
    model = Category
    context_object_name = 'categories'
    template_name = 'Main/SubCategoryList.html'


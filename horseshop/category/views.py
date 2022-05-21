from django.views.generic import ListView, DetailView
from category.models import Subcategory

class SubcategoryListView(ListView):
    model = Subcategory

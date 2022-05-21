from django.views.generic import ListView, DetailView

# from category.models import Category
from category.models import Subcategory

class SubcategoryListView(ListView):
    model = Subcategory

class CategoryDetailView(DetailView):
    model = Subcategory

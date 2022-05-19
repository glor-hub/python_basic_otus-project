from django.views.generic import ListView

from category.models import Category

class CategoryListView(ListView):
    model = Category
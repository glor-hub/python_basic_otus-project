from django.views.generic import ListView
from category.models import Subcategory

class SubcategoryListView(ListView):
    model = Subcategory

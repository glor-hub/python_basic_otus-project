from django.urls import path

import category.views as category

app_name = 'category'

urlpatterns = [
    path('', category.SubcategoryListView.as_view(), name='list'),
 ]

from django.urls import path

import category.views as category

app_name = 'category'

urlpatterns = [
    path('list/', category.CategoryListView.as_view(), name='list'),
]

from django.db import models

from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

class Subcategory(models.Model):
    name = models.CharField(max_length=32, unique=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=32, db_index=True, unique=True, null=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

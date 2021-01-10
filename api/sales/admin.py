from django.contrib import admin
from sales import models

admin.site.register(models.Product)
admin.site.register(models.Category)

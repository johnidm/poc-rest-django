from django.contrib import admin
from quickstart import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Category, Listing, Like, Report
from django.db import models
#from . import forms
from ckeditor.widgets import CKEditorWidget

class ListingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Like)
admin.site.register(Report)
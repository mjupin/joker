from django.contrib import admin
from .models import TestResult, BrowserReport
# Register your models here.

class BrowserInline(admin.StackedInline):
    model = BrowserReport

class ResultAdmin(admin.ModelAdmin):
    inlines = [BrowserInline]

admin.site.register(TestResult, ResultAdmin)
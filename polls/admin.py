# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Question, Choice

from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['pub_date', 'question_text' ]}),
        ('Date information', {'fields' : ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

    search_fields = ['question_text']
admin.site.register( Question, QuestionAdmin )

# admin.site.register( Choice )
# Register your models here.

from django.contrib import admin
from django.contrib.admin.helpers import Fieldset

from .models import Question, Choice

admin.site.site_header = 'Poll Site'
admin.site.site_title = 'Admin Area'
admin.site.index_title = 'Welcome to the Poll admin area'

#from tutorial to link the choices to the question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# from documentation
    # admin.site.register(Question)
    # admin.site.register(Choice)

# add questions from backend
# add admin functionality

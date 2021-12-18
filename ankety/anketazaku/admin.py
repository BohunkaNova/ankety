from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Answers

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text', 'answers', 'rightone']}),
    ]

    list_display = ('question_text',)

class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['answer_text', ]}),
    ]

    list_display = ('answer_text',)



admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers, AnswerAdmin)

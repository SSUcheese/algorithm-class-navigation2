from django.contrib import admin
from .models import Route, Question, Choice

class RouteAdmin(admin.ModelAdmin):
    list_display = ['id','start_point', 'end_point', 'route']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','question_text']
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id','choice_text','question', 'votes']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Choice, ChoiceAdmin)

from django.contrib import admin

from .models import Game, Question

class QuestionAdmin(admin.ModelAdmin):
   list_display = ('question_text', 'correct_answer', 'incorrect_answers', 'game_id','question_number')
   #search_fields = ['question_text']

class GameAdmin(admin.ModelAdmin):
   list_display = ('name', 'category', 'difficulty', 'startdate', 'enddate')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Game, GameAdmin)


from django.db import models

from django.db import models

import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=255)
    startdate = models.TimeField()
    enddate = models.TimeField()
    difficulty = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Question(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default='', blank=False)
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    incorrect_answers = models.CharField(max_length=255)
    question_number = models.IntegerField(default=0)

    def get_incorrect(self):
       return str.split(self.incorrect_answers, ",")

    # def __str__(self):
    #     return self.question_text
	
	def test_game(self):
        return self.game
	
	def test_question_text(self):
        return self.question_text

	def test_correct_answer(self):
        return self.correct_answer
		
	def test_incorrect_answers(self):
        return self.incorrect_answers
	
	def test_question_number(self):
        return self.question_number
	
	
	

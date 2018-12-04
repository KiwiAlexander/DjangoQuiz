
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import requests
import json
import urllib.request
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import SignUpForm
from .models import Question, Game
import datetime
from random import shuffle


# Create your views here.
#Home Page Shows user
def index(request):
    if request.user.is_authenticated:
        return render(request, 'quiz/index.html')
    else:
        return render(request, 'registration/login.html')

#Old Dataview Page unused in final
def dataView(request):
    #Building a URL to pass to requests
    jsonList = []
    jsonURL = "https://opentdb.com/api.php?amount=10"
    with urllib.request.urlopen(jsonURL) as url:
        result = json.loads(url.read().decode())
        jsonList.append(result)
    parsedData = []
    #Grabbed the JSON data forom request and reading it as JSON
    print(jsonList)
    #Breaking the JSON data up and saving the fields to our database question
    for data in jsonList[0]['results']:
        newQuestion = Question()
        newQuestion.category = data['category']
        newQuestion.type = data['type']
        newQuestion.difficulty = data['difficulty']
        newQuestion.question_text = data['question']
        newQuestion.correct_answer = data['correct_answer']
        incorrectAnswers = []
        #the incorrect answers is an array so splitting them up and adding correct answer
        for tempAnswer in data['incorrect_answers']:
            incorrectAnswers.append(tempAnswer)
        newQuestion.incorrect_answers = data['incorrect_answers']
        newQuestion.save()
    return render(request, 'quiz/dataView.html')

#Using django forms default reg form
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/quiz/')
    else:
        form = SignUpForm()
    return render(request, 'quiz/signup.html', {'form': form})

#Lists out the availible games
def game(request):
    gamelist = Game.objects.filter()
    return render(request, 'quiz/game.html', {'gamelist': gamelist})

#Lists the questions to play the quiz
def playgame(request, pk, qnum):
    currentgame = Game.objects.get(pk=int(pk))
    currentgamecat = currentgame.category
    currentgamecat = str(currentgamecat)

    #Calls a function that picks the JSON url for the cat the user picked
    jsonURL = pickCategory(currentgamecat)
    #Creates the questions and fills in the DB
    createQuestions(jsonURL , pk)
    #Takes the last 10 questions in the database made for that cat
    questionList = Question.objects.filter(game_id=pk).order_by('-game_id')[:10]
    #splits the answers and adds correct
    incorrectAnswers = []
    for question in questionList:
        splitAns = str.split(question.incorrect_answers, ",")

        for i in splitAns:
            incorrectAnswers.append(splitAns[splitAns.index(i)])
       
        incorrectAnswers.append(question.correct_answer)

    return render(request, 'quiz/playgame.html', {'questionList' : questionList, 'incorrectAnswers' : incorrectAnswers})

#Changes the URL with the selected cat
def pickCategory(currentgamecat):
    jsonURL = "https://opentdb.com/api.php?amount=10"
    if currentgamecat == "GeneralKnowledge":
        jsonURL = "https://opentdb.com/api.php?amount=10&category=9&type=multiple"

    elif currentgamecat == "Books":
        jsonURL = "https://opentdb.com/api.php?amount=10&category=10&type=multiple"
    
    elif currentgamecat == "Film":
        jsonURL = "https://opentdb.com/api.php?amount=10&category=11&type=multiple"

    elif currentgamecat == "Music":
        jsonURL = "https://opentdb.com/api.php?amount=10&category=12&type=multiple"

    elif currentgamecat == "MusicalTheatres":
        jsonURL = "https://opentdb.com/api.php?amount=10&category=13&type=multiple"

    elif currentgamecat == "Television":
        jsonURL = "https://opentdb.com/api.php?amount=10&category=14&type=multiple"

    elif currentgamecat == "ScienceNature":
        jsonURL = "https://opentdb.com/api.php?amount=10&category=17&type=multiple"

    elif currentgamecat == "ScienceComputers":
        jsonURL = "https://opentdb.com/api.php?amount=10&category=18&type=multiple"
    return jsonURL

#Look at dataview for detail on this function
def createQuestions(jsonURL, pk):
    jsonList = []
    with urllib.request.urlopen(jsonURL) as url:
        result = json.loads(url.read().decode())
        jsonList.append(result)
    parsedData = []
    count = 1
    for data in jsonList[0]['results']:
        newQuestion = Question()
        newQuestion.game_id = pk
        newQuestion.category = data['category']
        newQuestion.type = data['type']
        newQuestion.difficulty = data['difficulty']
        newQuestion.question_text = data['question']
        newQuestion.question_number = count
        count = count + 1
        newQuestion.correct_answer = data['correct_answer']
        incorrectAnswers = []
        for tempAnswer in data['incorrect_answers']:
            incorrectAnswers.append(tempAnswer)
        newQuestion.incorrect_answers = data['incorrect_answers']
        newQuestion.save()

#Creates the game with a form which the user selects and makes the name the user name and time made
def createquiz(request):
    if request.method == 'POST':
        print("Create Quiz Working!")
        difficulty = request.POST.get("difficulty")
        category = request.POST.get("category")
        newGame = Game()
        gameName = (str(request.user) + str(datetime.datetime.now()))
        newGame.name = (gameName)
        newGame.startdate = datetime.datetime.now()
        newGame.enddate = datetime.datetime.now()
        newGame.difficulty = difficulty
        newGame.category = category
        newGame.save()

    return render(request, 'quiz/createquiz.html')

def scoreboard(request):
    return render(request, 'quiz/scoreboard.html')
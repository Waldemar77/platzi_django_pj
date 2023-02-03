from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# Create your views here.


def index(request):

    # In this variable, we get all questions from model object Question. 
    latest_question_list = Question.objects.all()

    # We returt the template from the templates/polls/index.html and we indicate the variables we need to use. 
    return render(request, 'polls/index.html', {
        "latest_question_list":latest_question_list
    })


def number_question(request, id_question):
    
    # We're using the get_object_or_404 function to manage the error http when the consult is not effective.
    question_1 = get_object_or_404(Question, pk=id_question)
    return render(request, "polls/detail.html", {
        "question_1":question_1
    })


def results(request, id_question):
    return HttpResponse(f'You are watching the results for the number question: {id_question}')


def votes(request, id_question):
    return HttpResponse(f'You are voting for the number question: {id_question}')
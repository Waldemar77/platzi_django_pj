from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


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
    # We're using the get_object_or_404 function to manage the error http when the consult is not effective.
    question_1 = get_object_or_404(Question, pk=id_question)
    return render(request, 'polls/results.html', {
        "question_1" : question_1
    })


def votes(request, id_question):
    
    # firstly, we must call a object of Question model
    question_1 = get_object_or_404(Question, pk=id_question)

    # secondly, we manage the flow of the logic through try-except
    try:
        # Here, we use the function request.POST[] to get the data from the forms
        # according to the choice selected.
        # The POST[] dictionary call the key 'choice', related with the label name in the form.
        selected_choice = question_1.question_choices.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # If the user doesn't select some item, we render the same "detail" view but we add the
        # error_message variable to the view.
        return render(request, 'polls/detail.html', {
            "question_1":question_1,
            "error_message":"You must select some anwser. Please, select one item."
        })
    else:
        # If the user selected one item and the request.POST[] found the id, we can start the counter
        # in the attribute "votes" from Choice Model and save the result into the model (database).
        selected_choice.votes += 1
        selected_choice.save()
        
        # we'll redirect to the user to 'question_results' view through the function 
        # reverse(), this one is the same code "% url %" used in the templates, but 
        # now it's wroten in python 
        return HttpResponseRedirect(reverse('polls:question_results', args=(question_1.id,)))
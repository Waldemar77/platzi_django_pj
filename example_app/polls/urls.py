# file to store the url of our app

from django.urls import path, include
from . import views

# Variable with the main name of our url
app_name = 'polls'

"""
# urls settings to class generic views
urlpatterns = [
    #example: polls/
    path('', views.IndexView.as_view(), name='index'),
    
    #example: polls/1
    path('<int:pk>/detail', views.NumberQuestionView.as_view(), name='number_question'),

    #example: polls/1/results
    path('<int:pk>/results', views.ResultView.as_view(), name='question_results'),

    #example: polls/1/votes
    path('<int:id_question>/votes', views.votes, name='question_votes'),
]
"""
# urls settings to functions views
urlpatterns = [
    #example: polls/
    path('', views.index, name='index'),
    
    #example: polls/1
    path('<int:id_question>/detail', views.number_question, name='number_question'),

    #example: polls/1/results
    path('<int:id_question>/results', views.results, name='question_results'),

    #example: polls/1/votes
    path('<int:id_question>/votes', views.votes, name='question_votes'),
]

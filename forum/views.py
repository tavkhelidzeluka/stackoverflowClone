from django.shortcuts import render
from django.views.generic import ListView, DetailView

from forum.models import Question


# Create your views here.
class HomeView(ListView):
    model = Question
    template_name = 'forum/question_list.html'

class QuestionDetailView(DetailView):
    model = Question

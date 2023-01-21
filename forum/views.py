from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Question
from forum.forms import QuestionCreateForm


# Create your views here.
class HomeView(ListView):
    queryset = Question.objects.all()
    model = Question
    template_name = 'forum/question_list.html'

class QuestionDetailView(DetailView):
    model = Question


# def create_question_view(request):
#     if request.method == 'GET':
#         return render(
#             request, 
#             'forum/question_add.html', 
#             {
#                 'form': QuestionCreateForm()
#             }
#         )

#     print(request.POST)
#     form = QuestionCreateForm(request.POST)

#     if form.is_valid():
#         form.save()
#         return redirect('forum:home')
    
#     return render(
#         request, 
#         'forum/question_add.html', 
#         {
#             'form': form
#         }
#     )

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = [
        'title', 'text'
    ]
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/question_add.html'

    def form_valid(self, form):
        self.object: Question = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    

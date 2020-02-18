from django.shortcuts import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return  HttpResponse(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'quesion': question})

def results(request, question_id):
    response = (f"You're looking at the results of question {question_id}.")
    return HttpResponse(response, question_id)

def vote(request, question_id):
    return  HttpResponse(f"You're voting on question{question_id}.")

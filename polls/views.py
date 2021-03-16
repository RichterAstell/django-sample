from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question

# Create your views here.
def index(request):
    list = Question.objects.order_by('-pub_date')[:5]
    return render(
        request,
        'polls/index.html',
        {'list': list},
    )

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

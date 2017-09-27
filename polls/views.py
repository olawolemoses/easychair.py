# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Question, Choice

from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic

from django.utils import timezone

# def index( request ):
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.question_text for q in latest_question_list])
	#context = {'latest_question_list' : latest_question_list,}
#	return render( request, 'polls/index.html', context )

class IndexView( generic.ListView ):

    template_name = 'polls/index.html'

    context_object_name = 'latest_question_list'

    def get_queryset( self ):

        """Return the last five published questions."""

        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView( generic.DetailView ):

    model = Question

    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yes
        """

        return Question.objects.filter(pub_date__lte=timezone.now())
        

class ResultsView(generic.DetailView):

    model = Question

    template_name = "polls/results.html"


def detail(request, question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results( request, question_id ):
    question = get_object_or_404( Question, pk = question_id )
    return render(request, 'polls/results.html', {'question' : question })

def vote( request, question_id ):
    question = get_object_or_404( Question, pk=question_id )
    try:
        selected_choice = question.choice_set.get( pk=request.POST['choice'] )
    except (KeyError, Choice.DoesNotExist ):
        return render(request, 'polls/index.html', {
            'question': question,
            'error_message': "you didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse( "polls:results", args=(question.id, )))

from django.shortcuts import render, get_object_or_404 

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) 


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question}) 


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


# Begining of Django Rest Framework code
#
from rest_framework import viewsets, filters
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.authtoken.models import Token # to get/create tokens
from django.contrib.auth.models import User # to get/create tokens


class QuestionViewSet(viewsets.ModelViewSet ):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    View used by Choices API
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('votes', 'question_id')

def developer(request):
    if request.user.is_authenticated():
        token = Token.objects.get_or_create(user=User.objects.get(username='admin'))
        data = token
    else:
        data = 'You must be logged in to use this page.'
    return render(request, 'polls/developer.html', {'data': data})
    
# End of DRF code
#
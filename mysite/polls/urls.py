from django.conf.urls import url, include # "included" added for DRF

from . import views

from rest_framework import routers # line added for DRF


router = routers.DefaultRouter() # line added for DRF
router.register(r'questions', views.QuestionViewSet) #line added for DRF


urlpatterns = [
    url(r'^api/', include(router.urls)), # line added for DRF, Wire up our API using automatic URL routing.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # line added for DRF, Additionally, we include login URLs for the browsable API.
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]


# The API can be accessed thru the DRF browseable interface at http://127.0.0.1:8000/polls/api/questions
# or if thru console with the command $curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/polls/api/questions/
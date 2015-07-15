from django.conf.urls import url, include # "included" added for DRF

from . import views

from rest_framework import routers # line added for DRF


router = routers.DefaultRouter() # line added for DRF
router.register(r'questions', views.QuestionViewSet) #line added for DRF
router.register(r'choices', views.ChoiceViewSet) #line added for DRF


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
    # ex: /polls/developers
    url(r'^developer/$', views.developer, name='developer'),
]


# The API can be accessed thru the DRF browseable interface at http://127.0.0.1:8000/polls/api/questions
#
# or if thru console:
#
# CREATE 
# $ curl -d "question_text=api created&pub_date=2013-01-29T12:34:56.123Z" http://127.0.0.1:8000/polls/api/questions/
#
# RETRIEVE
# $ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/polls/api/questions/
# 
# RETRIEVE WITH TOKEN
# $ curl -X GET -H 'Accept: application/json; indent=4' -H 'Authorization: Token 3f7ea2dbe3c2cab9b55346200d7ef4796f53c731' http://127.0.0.1:8000/pols/api/questions/
#
# UPDATE
# $ curl -X PUT -d "question_text=ble ble ble&pub_date=2015-06-25T21:52:17Z" http://127.0.0.1:8000/polls/api/questions/6/
#
# DELETE
# $ curl -X DELETE http://127.0.0.1:8000/polls/api/questions/5/
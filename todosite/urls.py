from django.conf.urls import url, include
from django.contrib import admin
from todo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Registration for new users
    url(r'^register/$', views.RegistrationView.as_view()),

    # # Todos endpoints
    url(r'^todos$', views.TodosView.as_view()),
    url(r'^todos/(?P<todo_id>[0-9]*)$', views.TodosView.as_view()),

    # # AnswerKey endpoint
    url(r'^answer_key$', views.AnswerKeyView.as_view()),

    # # API Auth
    # url(r'^oauth2/$', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]

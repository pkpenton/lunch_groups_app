from django.conf.urls import url
from teamlunch.views import TeamLunchView

urlpatterns = [
    url(r'^$', TeamLunchView.as_view()),
]

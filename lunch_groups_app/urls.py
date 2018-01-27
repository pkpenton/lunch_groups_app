from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'', include('teamlunch.urls')),
    url(r'^teamlunch/', include('teamlunch.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]

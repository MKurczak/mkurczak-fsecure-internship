from django.urls import path
from .views import randomView, echoView, listView
#Both paths are with and without trailing slashes "/" to simplicy testing. 
#Browser will add trailing slash automatically but for Django thats two separate URL's.
#There is option to automatically append slashed at the end of path but it may caus malfunctioning of POST method used here.
urlpatterns = [
    path('random/', randomView.randomPage, name='randomPage'),
    path('random', randomView.randomPage, name='randomPage'),
    path('echo/', echoView.echo, name='echo'),
    path('echo', echoView.echo, name='echo'), 
    path('list/', listView.listPage, name='list'),
    path('list', listView.listPage, name='list'),
]
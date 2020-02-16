from django.http import HttpResponse
from app.models import listModel

#Return all objects from database if they exist.
def listPage(request):
    return HttpResponse(listModel.objects.values())

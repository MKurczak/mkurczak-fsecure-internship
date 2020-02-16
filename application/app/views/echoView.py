from django.http import JsonResponse
from app.models import listModel
import json
#!!!!!!
#This snippet is used to exempt this view from CSRF (Cross Site Request Forgery) protection.
#Which means there is no need of having CSRF tokens while using POST method.
#WARNING! THIS IS SOLELY FOR DEVELOMPENT PURPOSE AND IS NOT MEANT TO BE USED ON PRODUCTION ENVIRONMENT.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
#!!!!!!
def echo(request):
    # Check if requesting method is POST
    if request.method == 'POST':
        #Add entry to database if POST method is invoked.
        listModel.objects.create(randomEntry="firstentry", anotherRandomEntry="test")
        #Test if incoming JSON is correct
        try:
            setStatus = "ok"
            setMsg = json.loads(request.body)
        #Rise error when incoming JSON is malformed.
        except Exception as exceptionError:
            setStatus = "error"
            setMsg = str(exceptionError)
        #Return JSON and POST'ed message as JSON.
        jsonMsg = {
            "status": setStatus,
            "msg": setMsg
        }
        return JsonResponse(jsonMsg)
    #Check if requesting method is GET.
    elif request.method == 'GET':
        json_msg2 = {
            "status": "error",
            "msg": "Please use POST method to view this page functionality."
        }
        return JsonResponse(json_msg2)
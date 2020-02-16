from django.http import JsonResponse
import random

#Return random number on request in JSON format.
def randomPage(request):
    rng_json = {
        "status": "ok",
        "number": str(random.randrange(0, 100))
    }
    return JsonResponse(rng_json)
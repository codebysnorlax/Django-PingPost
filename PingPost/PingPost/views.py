from django.http import JsonResponse

def home(request):
    data = {
        'status': 'success',
        'message': 'Hello from Django!',
        'user': 'snorlax'
    }
    return JsonResponse(data)

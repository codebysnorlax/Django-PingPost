from django.http import JsonResponse

def home(request):
    data = {
    'status': 'success',
    'message': 'Hello from Django!',
    'user': 'snorlax',
    'Hint': {
        'type': '/tweet',
        'for': 'navigate to main page'
    }
}

    return JsonResponse(data)

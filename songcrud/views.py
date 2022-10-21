from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello there !, this is Songcrud, my first Django app')


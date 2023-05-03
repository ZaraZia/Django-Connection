from django.http import HttpResponse
def index(request):
    return HttpResponse("text for branch 2, changing for second time to check.")
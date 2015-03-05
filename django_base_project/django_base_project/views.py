from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from django! Try out <a href='/admin/'>/admin/</a>\n")
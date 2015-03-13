from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello %s! Try out <a href='/admin/'>/admin/</a>\n" % request.user)

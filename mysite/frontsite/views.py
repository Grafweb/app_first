from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontsite/index.html')

def hello(request):
    return render(request, 'frontsite/partials/hello.html')
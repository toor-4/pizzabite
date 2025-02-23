from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pizza/index.html')


def about(request):
    return render(request, 'pizza/about.html')
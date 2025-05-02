from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html') # This view renders the index.html template located in the base/templates/base directory.
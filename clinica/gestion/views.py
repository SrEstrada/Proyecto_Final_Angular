from django.shortcuts import render

# Create your views here.
def angular_app(request):
    return render(request, 'index.html')
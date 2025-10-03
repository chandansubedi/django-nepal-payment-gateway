from django.shortcuts import render

# Create your views here.
def success(request, id):
    return render(request, 'esewa/success.html', {'id': id})

def failure(request, id):
    return render(request, 'esewa/failure.html', {'id': id})    
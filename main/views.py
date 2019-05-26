from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def self(request):
    return render(request, 'self.html')
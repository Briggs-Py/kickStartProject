from django.shortcuts import render

def home(request):
  return render(request, 'kickstart/index.html', {})

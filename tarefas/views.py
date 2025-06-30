from django.shortcuts import render

# Create your views here.

def listatarefas(request):
    return render(request, 'tarefas/lista.html')
from django.shortcuts import render
from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm()
    
    contexto = {
        'form': form
    }
    return render(request, 'contato.html', contexto)

def produto(request):
    return render(request, 'produto.html')
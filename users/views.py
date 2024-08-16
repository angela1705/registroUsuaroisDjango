from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

# Create your views here.

def registrerUser(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarUsuarios')
        else:
            form =PersonaForm()
            return render (request, 'registroUsuario.html', {'form': form})





from django.shortcuts import render, redirect
from .form import MeuFormulario
from .models import Portfolio

def projeto_view(request):
    projeto = Portfolio.objects.all()
    search = request.GET.get('search')

    if search:
        projeto = Portfolio.objects.filter(name__contains= search)
    return render(request, 'resultados.html', {'projeto' : projeto}) 

def form_view(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projeto_view')
    else:
        form = MeuFormulario()
    return render(request, 'formulario.html', {'form': form})
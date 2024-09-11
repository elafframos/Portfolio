from django.shortcuts import render, redirect
from .form import MeuFormulario
from .models import Resultado, Portfolio

def form_view(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('mostrar_resultados')
    else:
        form = MeuFormulario()
    return render(request, 'formulario.html', {'form': form})

def formulario_view(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST)
        if form.is_valid():
            variavel1 = form.cleaned_data['variavel1']
            variavel2 = form.cleaned_data['variavel2']
            variavel3 = form.cleaned_data['variavel3']
            
            # Cria uma nova instância do modelo Resultado
            Resultado.objects.create(
                variavel1=variavel1,
                variavel2=variavel2,
                variavel3=variavel3
            )
            
            return redirect('resultados.h')  # Redireciona para a página de resultados
    else:
        form = MeuFormulario()
    
    return render(request, 'formulario.html', {'form': form})

def mostrar_resultados(request):
    resultados = Resultado.objects.all()
    return render(request, 'resultados.html', {'resultados': resultados})

def projeto_view(request):
    projeto = Portfolio.objects.all()
    search = request.GET.get('search')

    if search:
        projeto = Portfolio.objects.filter(name__contains= search)
    return render(request, 'resultados.html', {'projeto' : projeto})                                                                        

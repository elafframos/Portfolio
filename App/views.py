from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .form import MeuFormulario
from .models import Portfolio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def projeto_view(request):
    projeto = Portfolio.objects.all()
    search = request.GET.get('search')

    if search:
        projeto = Portfolio.objects.filter(name__contains= search)
    return render(request, 'resultados.html', {'projeto' : projeto}) 

@login_required(login_url="/login/")
def form_view(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projeto_view')
    else:
        form = MeuFormulario()
    return render(request, 'formulario.html', {'form': form})

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usúario com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('projeto_view')
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return redirect('projeto_view')
        else:
            return HttpResponse('Email ou senha inválidos')

@login_required(login_url="/login/")
def editar_item(request, id):
    item = get_object_or_404(Portfolio, id=id)
    if request.method == "POST":
        form = MeuFormulario(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('projeto_view')  # Redireciona para a lista de itens após salvar
    else:
        form = MeuFormulario(instance=item)
    return render(request, 'editar_item.html', {'form': form})


def excluir_item(request, id):
    item = get_object_or_404(Portfolio, id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('projeto_view')  # Redirecione após a exclusão

    return render(request, 'confirmar_exclusao.html', {'item': item})

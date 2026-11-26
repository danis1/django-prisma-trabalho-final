from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
#form do usuario
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from .forms import CadastroForm


# Create your views here.


@login_required #protege a rota só para usuario logado
def dashboard(request):
    
    if request.user.is_superuser:
        return redirect("/admin/")


    #if perfil.tipo_usuario == 'administrador':
        #return redirect ("/admin/")

    return render(request, "dashboard.html")




@login_required
def perfil(request):
            

    if request.method == "POST":
        
        usuario = request.user

        usuario.first_name = request.POST.get("nome")
        usuario.last_name = request.POST.get("sobrenome")
        usuario.email = request.POST.get("email")

        usuario.save()

        return redirect("perfil")

    return render(request, "perfil.html")


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario,tipo_usuario='cliente')
            return redirect('login')

    else:
        form = CadastroForm()
        
    return render(request, 'cadastro.html', {'form': form})













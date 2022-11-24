
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from tienda.forms import customUserForm

def registro(request):
    form = customUserForm()
    if request.method == 'POST':
        form = customUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente")
            return redirect('/login')
    context = {'form':form}
    return render(request, 'tienda/auth/registro.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "ya te encuentras logeado :)")
        return redirect('/')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Inicio de sesion correto")
                return redirect("/")
            else:
                messages.error(request, "usuario o contraseña incorrectas")
                return redirect('/login')
        return render(request, "tienda/auth/login.html")
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Sesion cerrada correctamente")
    return redirect("/")

        
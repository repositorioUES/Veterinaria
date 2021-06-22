from django.shortcuts import redirect, render,get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Registro exitoso")
            return redirect(to="index")
        data["form"]=formulario

    return render(request, 'registration/registro.html',data)
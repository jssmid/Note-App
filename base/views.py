from django.shortcuts import render , redirect
from .models import Note
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .forms import NoteForm , UserCreateForm
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(owner=request.user)
        context = {'notes': notes}
        return render(request, 'home.html', context)
    else:
        return redirect('login')
    


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    context = {}
    return render(request, 'login_page.html' ,context)


def logoutPage(request):
    logout(request)
    return redirect('login')

def signUpPage(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'signup_page.html' ,context)


def addNote(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.owner = request.user
            saving.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'fill_form.html' ,context)



@login_required(login_url='login')
def editNote(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'fill_form.html' ,context)


def deleteNote(request, pk):
    note = Note.objects.get(id=pk).delete()
    return redirect('home')
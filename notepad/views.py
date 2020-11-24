from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from .forms import Noteform
# Create your views here.

# homepage
def home(request):
    finished_notes = Note.objects.filter(completed=True)
    unfinished_notes = Note.objects.filter(completed=False)
    context = {
        'finished_notes': finished_notes,
        'message': 'Note has been deleted!',
        'unf_notes': unfinished_notes
    }
    return render(request, 'home.html', context)

def signupuser(request):
   if request.method == "GET":
        return render(request, 'signupuser.html', {'form': UserCreationForm()})
   else:
        # create new user
        if request.POST['password1'] == request.POST['password2']: 
            try: 
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('home')

            except IntegrityError:
                return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error':'A User with that name already excist'})                    
        else:
             return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error':'A User with that name already excist'})                  

  

def finished_note(request, id):
    note = get_object_or_404(Note, pk=id)
    note.completed = True
    note.save()
    return redirect('home')

def unfinished_note(request, id):
    note = get_object_or_404(Note, pk=id)
    note.completed = False
    note.save()
    return redirect('home')

# get details of a note
def detail(request, id):
    note_details = get_object_or_404(Note, pk=id)
    context = {
        'note': note_details
    }
    return render(request, 'detail.html', context)

# Create a note
def create(request):
    if request.method == 'POST':
        form = Noteform(request.POST)
        form.save()
        return redirect('home')
    else:
        form = Noteform()

    return render(request, 'create.html', {'form': form})

# Update a note
def update(request, id):
    note = get_object_or_404(Note, pk=id)

    if request.method == 'POST':
        form = Noteform(request.POST, instance=note)
        form.save()
        return redirect('home')

    else:
        form = Noteform(instance=note)
    
    context = { 'form': form, 'note': note }
    return render(request, 'update.html', context) 

def delete(request, id):
    note = get_object_or_404(Note, pk=id)
    note.delete()
    return redirect('home')

def loginuser(request):
   if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'loginuser.html', {'form': AuthenticationForm(), 'error':'Wrong Credentials.' }) 
   else:
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})       

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')           

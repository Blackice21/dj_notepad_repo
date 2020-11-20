from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Note
from django.contrib.auth.models import User
from .forms import Noteform, Userform
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
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Userform()
        return render(request, 'signupuser.html', {'form':form})

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

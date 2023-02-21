from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.

#tasks = ['foo', 'bar', 'baz']
class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')

# def index(request):
#     return render(request, 'tasks/index.html', {
#         'tasks': tasks
#     })
def index(request):

    if 'tasks' not in request.session:
        request.session['tasks'] = []
        
    details = [request.session['tasks'], type(request.session['tasks'])]
    
    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasks'], 'details': details
    })

# def add(request):
#     return render(request, 'tasks/add.html')
#------------------------------------------------
# def add(request):
#     return render(request, 'tasks/add.html', {
#         "form": NewTaskForm()
#     })
def add(request):
    if request.method == "POST":

        form = NewTaskForm(request.POST)

        if form.is_valid():
            
            task = form.cleaned_data['task']

            #tasks.append(task)
            #----------1st Method---------
            # tasks = request.session.get('tasks', [])
            # tasks = request.session['tasks']
            # tasks.extend([task])
            # request.session['tasks'] = tasks
            #---------2nd Method------------
            request.session['tasks'] += [task]

            return HttpResponseRedirect(reverse("tasks:index"))
        
        else:
            return render(request, 'tasks/add.html', {
                'form': form
            })
    
    return render(request, 'tasks/add.html', {
        'form': NewTaskForm()
    })
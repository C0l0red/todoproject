from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem

# Create your views here.
def todoappView(request):
    return render(request, 'todolist.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 

def addTodoView(request):
    content = request.POST['content']
    new_item = TodoListItem(content = content)
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 

def deleteTodoView(request, id):
    item = TodoListItem.objects.get(id= id)
    item.delete()
    return HttpResponseRedirect('/todoapp/') 
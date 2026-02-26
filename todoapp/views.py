from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect

# Create your views here.


def todoAppView(request):
    all_todo_items = TodoListItem.objects.all()
    
    return render(request,'todoList.html', {'all_items': all_todo_items})

def addTodoItem(reuqest):
    x = reuqest.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoItem(reuqest, i):
    y = TodoListItem.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')

def editTodoItem(reuqest, i):
    TodoListItem.objects.update(edit = False)
    y = TodoListItem.objects.get(id = i)
    y.edit = True
    y.save()
    return HttpResponseRedirect('/todoapp/')

def saveTodoItem(request, i):
    item = TodoListItem.objects.get(id=i)
    item.content = request.POST["content"]
    item.edit = False
    item.save()
    return HttpResponseRedirect('/todoapp/')
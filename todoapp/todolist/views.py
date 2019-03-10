from django.shortcuts import render, redirect
from .models import TodoList, Category

# Create your views here.
def index(request): # the index view
    todos = TodoList.objects.all() # quering all the todos with the object manager
    categories = Category.objects.all() # getting all the categories with the object manager

    if request.method == "POST": # check if the request method is a post
        if "taskAdd" in request.POST: #check to see if there is a request to add atodo
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + "--" + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/") # reload the page

        if "taskDelete" in request.POST: # check if there is a request to delete atodo
            checklist = request.POST["checkedbox"] # check todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #then delete a todo
    return render(request, "index.html", {"todos":todos, "categories":categories})
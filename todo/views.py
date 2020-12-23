from django.shortcuts import render

# Create your views here.


# todo list View.
def todo_list(request):
    context = {
        'developer': 'Mohammed Elkhamlichi',
    }
    return render(request, 'todo/todo_list.html', context)
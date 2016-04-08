from django.shortcuts import render
from django.template import loader
from .forms import TodoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import Todo
from django.core.urlresolvers import reverse


def index(request):
    latest_work_list = Todo.objects.all()
    context = {'work_info': latest_work_list}
    return render(request, 'todolist/index.html', context)



def add_work(request):
    if request.method=="POST":
	temp_work=request.POST.get("work","")
        new_work=Todo(work_list=temp_work)
	new_work.save()
    return HttpResponseRedirect(reverse('todolist:index'))
    


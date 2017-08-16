from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def home_page(request):
	unfinished_tasks = Task.objects.filter(completed=False).order_by("-create_time")
	finished_tasks = Task.objects.filter(completed=True).order_by("-create_time")
	return render(request, 'home_page.html', {'unfinished_tasks':unfinished_tasks, 'finished_tasks':finished_tasks})

def add_task(request):
	task_title = request.POST.get("title")
	if task_title is not None:
		task = Task.objects.create(title=task_title)
	return redirect(home_page)

def complete_task(request, pk):
	task = Task.objects.filter(pk=pk)
	if task.exists():
		task = task.first()
		task.completed = True
		task.save()
	return redirect(home_page)

def about_page(request):
	return render(request, 'about_page.html')
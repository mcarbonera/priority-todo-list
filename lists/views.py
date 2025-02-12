from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
	return render(request, 'home.html')

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'list.html', {'list': list_})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=getText(request), priority=getPriority(request), list=list_)
	return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=getText(request), priority=getPriority(request), list=list_)
	return redirect(f'/lists/{list_.id}/')

def getText(request):
	return request.POST['item_text']

def getPriority(request):
	return request.POST['item_priority']
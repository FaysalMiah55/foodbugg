from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ItemForms
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# function based view for index
def index(request):
  item_list = Item.objects.all()
  context={
    "item_list" : item_list,
  }
  return render(request, "food/index.html", context)

# class based for index
class IndexClassViews(ListView):
  model = Item
  template_name = 'food/index.html'
  context_object_name = 'item_list'


def about(request):
  return render(request, "food/about.html")

# function based view for food detail
def detail(request, item_id):
  item = Item.objects.get(pk=item_id)
  context={
    'item': item,
  }
  return render(request, "food/detail.html", context)

# class based for food detail
class FoodDetail(DetailView):
  model = Item
  template_name = 'food/detail.html'

# function based view for create item
def createItem(request):
  form = ItemForms(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect("food:index")
  
  return render(request, "food/form_items.html", {'form':form})

# class based view for create item
class CreatItem(CreateView):
  model = Item
  fields = ['item_name', 'item_desc', 'item_price', 'item_image']
  template_name = 'food/form_items.html'
  def formValid(self, form):
    form.instance.user_name = self.request.user
    return super().form_valid(form)

def updateItem(request, id):
  item = Item.objects.get(id=id)
  form = ItemForms(request.POST or None, instance=item)

  if form.is_valid():
    form.save()
    return redirect("food:index")
  
  return render(request, "food/form_items.html", {'form':form, 'item':item})

def deleteItem(request, id):
  item = Item.objects.get(id=id)

  if request.method=="POST":
    item.delete()
    return redirect("food:index")
  
  return render(request, "food/delete_item.html", {'item':item})
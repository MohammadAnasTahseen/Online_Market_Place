from audioop import reverse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from items.models import *
from .forms import EditItemForm, NewItemForm
# Create your views here.


def items(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category',0)
    category=Category.objects.all()
    items=Item.objects.filter(is_sold=False)
    
    
    if category_id:
        items=items.filter(category_id=category_id)
    
    
    if query:
        items=items.filter(Q(name__icontains=query)| Q(description__icontains=query))
    return render(request,'items/items.html',{
        
        'items':items,
        'queries':query,
        'categories':category,
        'category_id':int(category_id)
    })
    
    
    
    
def detail(request,pk):
    print("geto s")
    item=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'items/details.html',{
        'items':item,
        'related_items':related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form=NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            # detail_url = reverse('detail', args=[item.pk])
            # return redirect(detail_url)
            return redirect('items:detail', pk=item.id)
    else:
        form=NewItemForm()
    return render(request,'items/form.html',{
        'forms':form,
        'titles':'New Item',
    })

@login_required
def Edit(request, pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form=EditItemForm(request.POST, request.FILES,instance=item)
        
        if form.is_valid():
            form.save()
         
            # detail_url = reverse('detail', args=[item.pk])
            # return redirect(detail_url)
            return redirect('items:detail', pk=item.id)
    else:
        form=EditItemForm(instance=item)
    return render(request,'items/form.html',{
        'forms':form,
        'titles':'Edit Item',
    })    
    
@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    
    return redirect ('dashboard:index')
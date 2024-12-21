from django.shortcuts import render
from django.shortcuts import redirect
from items.models import *
from .forms import SignupForm

# Create your views here.
def index(request):
    Items=Item.objects.filter(is_sold=False)[0:6]
    Categories=Category.objects.all()
    return render(request,'core/index.html',{
        
        'categories' : Categories,
        'items':Items,
        
    })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=SignupForm()
    return render(request,'core/signup.html',{
        'form':form
        
    })
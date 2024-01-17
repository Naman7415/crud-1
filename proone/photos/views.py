from django.shortcuts import render,redirect
from photos.forms import Find
from django.http import HttpResponse
from .models import Author
# Create your views here.

def create(request):
    if request.method=='POST':
        form= Find(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("views")    
    else:
        form=Find()
        return render(request,"index.html",{'form':form})
    
def view(request):
    if request.method=='GET':
        data = Author.objects.filter(active=True)
        return render(request,"home.html",{'data':data}) 

def update(request,id):
    data=Author.objects.get(id=id)
    form=Find(request.POST,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        return redirect("views")
    else:
        form=Find(instance=data)
    return render(request,"update.html",{'form':form})


def delete(request,id):
    datamodel=Author.objects.get(id=id)
    datamodel.active= False   
    datamodel.save()
    
            
    return redirect("views") 
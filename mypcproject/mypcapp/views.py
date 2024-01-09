from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models  import Mypc
from . forms import MypcForm

# Create your views here.
def index(request):
    mypc=Mypc.objects.all()
    context={
        'mypc_list':mypc
    }
    return render(request,'index.html',context)
def detail(request,mypc_id):
    mypc=Mypc.objects.get(id=mypc_id)
    return render(request,"detail.html",{'mypc':mypc})

def add_mypc(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        mypc=Mypc(name=name,desc=desc,year=year,img=img)
        mypc.save()

    return render(request,'add.html')

def update(request,id):
    mypc=Mypc.objects.get(id=id)
    form=MypcForm(request.POST or None, request.FILES,instance=mypc)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'mypc':mypc})
def delete(request,id):
    if request.method=='POST':
        mypc=Mypc.objects.get(id=id)
        mypc.delete()
        return redirect('/')
    return render(request,'delete.html')

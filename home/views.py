from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':"this is variable",
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is service page")

def contact(request):
    return HttpResponse("this is contact page")
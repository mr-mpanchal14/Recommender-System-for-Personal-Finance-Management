from django.shortcuts import render,HttpResponse, redirect
from Base.models import Info
from .forms import InfoForm
from django.contrib import messages

# Create your views here.
def index(request):
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     age = request.POST.get('age')
    #     gender = request.POST.get('gender')
    #     education = request.POST.get('education')
    #     income = request.POST.get('income')
    #     fees = request.POST.get('fees')
    #     #predictions=request.POST.get('predictions')
    #     index = Info(name=name, age=age,gender=gender,education=education,income=income,fees=fees)
    #     index.save()
    #     messages.success(request, 'New entry received successfully!')
    

    if request.method == 'POST':  
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base-predictions')
    else:
        form = InfoForm()
    context = {
        'form': form,
    }
    return render(request,'index.html', context)
    # return HttpResponse("this is home page")
    
def predictions(request):
    final_predictions = Info.objects.all()
    context = {
        'final_predictions': final_predictions
    }
    return render(request, 'predictions.html', context)
    
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def contact(request):
    return render(request,'contact.html')
   # return HttpResponse("this is contact page")
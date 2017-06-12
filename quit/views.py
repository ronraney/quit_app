from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Thing
from .forms import ThingForm
from django.shortcuts import redirect
import datetime

# Create your views here.
  
def something_list(request):    
    if request.user.is_authenticated:
        things = Thing.objects.filter(quitter=request.user).filter(quit_date__lte=timezone.now()).order_by('quit_date')
        return render(request, 'quit/something_list.html', {'things': things})
    else: 
        return render(request, 'quit/base.html')

def thing_detail(request, pk):
    thing = get_object_or_404(Thing, pk=pk)
    return render(request, 'quit/thing_detail.html', {'thing': thing})
   
def thing_new(request):
    if request.method == "POST":
        form = ThingForm(request.POST) #call the ThingForm and pass it to the template
        if form.is_valid():
            thing = form.save(commit=False)
            thing.quitter = request.user
            thing.save()
            return redirect('thing_detail', pk=thing.pk)
    else:
        form = ThingForm()
    return render(request, 'quit/thing_edit.html', {'form': form}) #Pass it to the template

def thing_edit(request, pk):
    thing = get_object_or_404(Thing, pk=pk)
    if request.method == "POST":
        form = ThingForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.quitter = request.user
            thing.save()
            return redirect('thing_detail', pk=thing.pk)
    else:
        form = ThingForm(instance=thing)
    return render(request, 'quit/thing_edit.html', {'form': form})

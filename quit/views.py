from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Thing
import datetime


# Create your views here.
def something_list(request):
    things = Thing.objects.filter(quit_date__lte=timezone.now()).order_by('quit_date')
    return render(request, 'quit/something_list.html', {'things': things})

def thing_detail(request, pk):
    thing = get_object_or_404(Thing, pk=pk)
    return render(request, 'quit/thing_detail.html', {'thing': thing})
    

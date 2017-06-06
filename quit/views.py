from django.shortcuts import render
from django.utils import timezone
from .models import Thing

# Create your views here.
def something_list(request):
    things = Thing.objects.filter(quit_date__lte=timezone.now()).order_by('quit_date')
    return render(request, 'quit/something_list.html', {'things': things})
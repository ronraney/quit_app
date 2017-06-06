from django.shortcuts import render

# Create your views here.
def something_list(request):
    return render(request, 'quit/something_list.html', {})
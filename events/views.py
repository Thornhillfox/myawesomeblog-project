from django.shortcuts import render
from .models import Event

# Create your views here.
def homepage(request):
	events = Event.objects
	return render(request, 'events/homepage.html', {'events': events})
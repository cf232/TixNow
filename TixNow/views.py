from django.shortcuts import render
from django.http import HttpResponse
from .models import TixGet
from .forms import getEvents
import ticketpy
import django_tables2 as tables

# def TixReq(CreateView):
#     model = TixNow
#     fields = ('start','end','genre','zipcode')

def home(request):
    if request.method == 'POST':
        form = getEvents(request.POST)
        if form.is_valid():
            pass
        else:
            form = getEvents()
    else:
        form = getEvents()
    return render(request, 'home.html', {'form':form})

def search(request):
    tm_client = ticketpy.ApiClient('zrBJbt2dGaWQ8OCEJWIhvQ2sOGMhui7Q')
    genre = request.POST['genre']
    start = request.POST['start']
    end = request.POST['end']
    zipcode = request.POST['zipcode']

    page = tm_client.events.find(
        classification_name = genre,
        postal_code= zipcode,
        start_date_time= start + 'T20:00:00Z',
        end_date_time= end +'T20:00:00Z'
    ).limit()

    class EventTable(tables.Table):
        Event = tables.Column()
        Venues = tables.Column()
        Start = tables.Column()
        Price = tables.Column()
        Status = tables.Column()
        Classification = tables.Column()
        class Meta:
            attrs = {'class': "table table-hover"}

    eventlist = list()
    for event in page:
        new_dict = {
            "Event" : event.name,
            "Venues" : event.venues[0].name,
            "Start" : event.local_start_date,
            "Price" : event.price_ranges,
            "Status" : event.status,
            "Classification" : event.classifications[0]
        }
        eventlist.append(new_dict)


    table = EventTable(eventlist)
    return render(request, 'search.html', {'table':table})


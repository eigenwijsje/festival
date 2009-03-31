from django.shortcuts import get_object_or_404, render_to_response

from forms import RegistrationForm
from models import Event, Site, Software

def register(request, event_slug, site_slug):
    event = get_object_or_404(Event, slug=event_slug)
    site = get_object_or_404(Site, event__slug=event_slug slug=site_slug)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return render_to_response('installfest/registration_complete.html',
                {'event': event, 'site': site})
    else:
        form = RegistrationForm()
        form.fields['event'].queryset = Event.objects.filter(id=event.id)
        form.fields['event'].initial = event.id
        form.fields['site'].queryset = Site.objects.filter(id=site.id)
        form.fields['site'].initial = site.id
        form.fields['software'].queryset = Software.objects.filter(site=site)

    return render_to_response('installfest/registration_form.html',
        {'form': form, 'event': event, 'site': site})

def site_detail(request, event_slug, site_slug):
    site = get_object_or_404(Site, event__slug=event_slug, slug=site_slug)

    return render_to_response('installfest/site_detail.html', {'site': site})

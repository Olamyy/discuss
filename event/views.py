from django.shortcuts import render
from django.conf import settings


def index(request):
    project_name = settings.PROJECT_NAME
    project_short_about = settings.PROJECT_SHORT_DESC
    event_date = settings.EVENT_DATE
    event_venue = settings.EVENT_VENUE
    return render(request, 'TheDiscuss/staticfy/index.html', {'project_name': project_name, 'project_short_descr':
        project_short_about, 'event_date': event_date,
                                                              'event_venue': event_venue})

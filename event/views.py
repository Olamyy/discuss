import json
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os

from .models import Attendee, Contact, Sponsor


def index(request):
    project_name = settings.PROJECT_NAME
    project_short_about = settings.PROJECT_SHORT_DESC
    event_date = settings.EVENT_DATE
    event_venue = settings.EVENT_VENUE
    image = Sponsor.objects.all()
    return render(request, 'TheDiscuss/staticfy/index.html', {'project_name': project_name, 'project_short_descr':
        project_short_about, 'event_date': event_date, 'event_venue': event_venue, 'images': image})


@csrf_exempt
def register(request):
    if request.method == "POST":
        first_name, last_name, email, attendance, mobile_number = request.POST.get('first_name'), request.POST.get(
            'last_name'), \
                                                                  request.POST.get('email'), request.POST.get(
            'attendance'), \
                                                                  request.POST.get('mobile_number')
        check = Attendee.objects.filter(email=email).count()
        print(check)
        if check > 0:
            error = "The provided email has been registered."
            return JsonResponse(error, status=500, safe=False)
        else:
            attendee = Attendee.objects.create(first_name=first_name, last_name=last_name, email=email,
                                               attendance=attendance, mobile_number=mobile_number)
            if attendee:
                message = {'message': "Successfully registered for the event. Do check your email for more details."}
                attendee.save()
                return JsonResponse(message, status=200, safe=False)
            else:
                message = {'message': "An error occurred"}
                return JsonResponse(message, status=500, safe=False)


@csrf_exempt
def contact(request):
    if request.method == "POST":
        message, email = request.POST.get('message'), request.POST.get('email')
        contacts = Contact.objects.create(message=message, email=email)

        if contacts:
            message = {'message': ""}
            contacts.save()
        else:
            message = {'message': "An error occurred"}
        return JsonResponse(message, safe=False)

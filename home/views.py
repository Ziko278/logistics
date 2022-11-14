from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from datetime import datetime, timezone
from django.core.exceptions import PermissionDenied
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import reverse
from site_admin.models import *


class HomePageView(TemplateView):
    template_name = 'home/index.html'


class ServicePageView(TemplateView):
    template_name = 'home/service.html'


def track_shipment(request):
    tracking_id = request.GET['tracking_id']
    try:
        logistic = LogisticModel.objects.get(tracking_id=tracking_id)
    except LogisticModel.DoesNotExist:
        return redirect(reverse('message', kwargs={'status': 'wrong_id'}))

    if logistic:
        if logistic.tracking_pin:
            return redirect(reverse('track_locked', kwargs={'tracking_id': tracking_id}))
    context = {
        'logistic': logistic,
        'current_state': ShipmentProgressModel.objects.filter(shipment=logistic).last(),
        'delayed': datetime.now(timezone.utc) > logistic.departure_date
    }

    return render(request, 'home/logistic_detail.html', context)


def track_locked_shipment(request, tracking_id):
    try:
        logistic = LogisticModel.objects.get(tracking_id=tracking_id)
    except LogisticModel.DoesNotExist:
        return redirect(reverse('message', kwargs={'status': 'wrong_id'}))
    context = {
        'logistic': logistic,
        'current_state': ShipmentProgressModel.objects.filter(shipment=logistic).last(),
        'delayed': datetime.now(timezone.utc) > logistic.departure_date
    }
    if request.method == 'POST':
        pin = request.POST['pin']
        if pin == logistic.tracking_pin:

            return render(request, 'home/logistic_detail.html', context)
        return redirect(reverse('message', kwargs={'status': 'wrong_pin'}))

    return render(request, 'home/logistic_pin.html', context)


def message(request, status):
    context = {
        'status': status
    }
    return render(request, 'home/logistic_message.html', context)


def logistic_quote(request):
    if request.method == 'POST':
        location=request.POST['from']
        destination = request.POST['to']
        type = request.POST['type']

        if location == destination:
            recommended_mode='truck'
            alternative_mode = None
        elif type == 'Perishable':
            recommended_mode = 'flight'
            alternative_mode = None
        else:
            recommended_mode = 'ship'
            alternative_mode = 'flight'

        context = {
            'recommended_mode': recommended_mode,
            'alternative_mode':alternative_mode
        }
        return render(request, 'home/recommendation.html', context)
    context = {
        'location_list': LocationModel.objects.order_by('country__name')
    }
    return render(request, 'home/logistic_quote.html', context)

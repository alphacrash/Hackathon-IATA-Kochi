from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView

from flow.models import Ticket

import ndcapi.sunexpress as sunexpress

notification = 0


def index(request):
    return render(request, "flow/index.html", {})


def home(request):
    return render(request, "registration/login.html", {})


def acceptor(request):
    ticket = get_object_or_404(Ticket, pk=3)
    context = {
        'ticket': ticket,
        'notification': notification,
    }
    return render(request, "flow/acceptor.html", context)


class Profile(LoginRequiredMixin, ListView):
    template_name = "flow/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notification'] = notification
        return context

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        pnr = request.POST.get('pnr')
        ticket = sunexpress.get_ticket_details(pnr)
        Ticket(user=self.request.user, flight=ticket['airline'], flight_no=ticket['flightnumber'], source=ticket['source'],
               destination=ticket['destination'], date=ticket['date'], pnr=ticket['pnr']).save()
        return HttpResponseRedirect('/profile/')


def bumped(request):
    global notification
    notification = notification + 1
    return HttpResponseRedirect('/profile/')

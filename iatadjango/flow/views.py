from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.views.generic import CreateView, DetailView, ListView

from flow.models import Ticket

import ndcapi.sunexpress as sunexpress


def index(request):
    return render(request, "flow/index.html", {})


class Profile(LoginRequiredMixin, ListView):
    template_name = "flow/profile.html"

    def get_queryset(self):
        return get_list_or_404(Ticket, user=self.request.user)

    def post(self, request, *args, **kwargs):
        pnr = request.POST.get('pnr')
        ticket = sunexpress.get_ticket_details(pnr)
        Ticket(user=self.request.user, flight=ticket['airline'], flight_no=ticket['flightnumber'], source=ticket['source'],
               destination=ticket['destination'], date=ticket['date'], pnr=ticket['pnr']).save()
        return HttpResponseRedirect('/profile/')

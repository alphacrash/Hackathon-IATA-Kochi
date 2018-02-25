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


def accepted(request, pk=None):
    global notification
    if notification > 0:
        notification = notification - 1
    t = get_object_or_404(Ticket, pk=pk)
    t.volunteer = True
    t.save()
    print(t)
    print("Volunteer Change")
    return HttpResponseRedirect('/acceptor/{}'.format(pk))


class AcceptorView(DetailView):
    template_name = 'flow/acceptor.html'
    queryset = Ticket.objects.all()


class Profile(LoginRequiredMixin, ListView):
    template_name = "flow/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global notification
        if notification > 0:
            context['show_notification'] = True
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


def bumped(request, pk=None):
    global notification
    notification = notification + 1
    t = get_object_or_404(Ticket, pk=pk)
    t.bumped = True
    t.save()
    return HttpResponseRedirect('/profile/')

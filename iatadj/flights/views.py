from django.shortcuts import render


def home(request):
    context = {

    }
    return render(request, "home.html", context)


def user_profile(request):
    context = {

    }
    return render(request, "profile.html", context)


def flight_booking(request):
    context = {

    }
    return render(request, "booking.html", context)


def flight_details(request):
    context = {

    }
    return render(request, "flight_details.html", context)


def flight_confirmation(request):
    context = {

    }
    return render(request, "flight_confirmation.html", context)

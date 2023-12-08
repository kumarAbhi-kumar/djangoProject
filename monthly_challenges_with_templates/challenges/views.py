from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.


# Creating a python dictionary for recording monthly activities
monthly_challenge_dict = {
    "january": "Bath every day, sharp at 7:00 AM",
    "february": "Check thats your room is clean twice a day",
    "march": "Have a walk around the mountain side every morning",
    "april": "Establish a regular sleep schedule and stick to it as much as possible, even on weekends.",
    "may": "Dedicate 15 minutes each day to decluttering a small area of your home or office.",
    "june": "Engage in activities that connect you to nature, such as hiking, camping, or gardening.",
    "july": "Keep a gratitude journal and write down three things you're grateful for each day.",
    "august": "Challenge yourself to step outside your comfort zone and try something new.",
    "september": "Schedule time for activities that bring you joy and relaxation, such as reading, taking a bath, or getting a massage.",
    "october": "Volunteer your time to a cause you care about.",
    "november": "Engage in activities that allow you to express your creativity, such as writing, painting, or playing music.",
    "december": None
}


def index_view(request):
    months = list(monthly_challenge_dict.keys())
    
    return render(request, "challenges/index.htm", {
        "title": "Monthly Challenge",
        "months_list": months,
    })


def monthly_challenge_view_by_num(request, month):
    try:
        months = list(monthly_challenge_dict.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("monthly-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Not a valid month..!")


def monthly_challenge_view(request, month):
    challenge_text = monthly_challenge_dict[month]
    return render(request, "challenges/challenge.htm", {
        "title": month,
        "months": month,
        "challenge": challenge_text
    })
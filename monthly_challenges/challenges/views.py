from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges_dict = {
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
    "december": "Take time to reflect on your progress and accomplishments throughout the year."
}

# Create your views here.


def redirect_default(request):
    list_items = ""
    months = list(monthly_challenges_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        redirect_path = reverse('month-chall-num', args = [month])
        list_items += f"<li><a href=\"{redirect_path}\">{capitalized_month}</a></li>"

    return HttpResponse(f"<ul>{list_items}</ul>")


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges_dict.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-chall-num", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Not a valid month..!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        # return reder(request, "challenges/challenge.html")
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Thant's not a valid month")
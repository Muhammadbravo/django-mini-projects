from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


monthly_challeneges = {
    "january": "You're looking at the monthly challenges for january",
    "february": "You're looking at the monthly challenges for february",
    "march": "You're looking at the monthly challenges for march",
    "april": "You're looking at the monthly challenges for april",
    "may": "You're looking at the monthly challenges for may",
    "june": "You're looking at the monthly challenges for june",
    "july": "You're looking at the monthly challenges for july",
    "august": "You're looking at the monthly challenges for august",
    "september": "You're looking at the monthly challenges for september",
    "october": "You're looking at the monthly challenges for october",
    "november": "You're looking at the monthly challenges for november",
    # "december": "You're looking at the monthly challenges for december",
    "december": None
}

def index(request):
    months = list(monthly_challeneges.keys())
    return render(request, "challenges/index.html", {"months": months})

def monthly_challenge_by_number(request, month):
    months = list(monthly_challeneges.keys())

    if month > len(months):
        return HttpResponseNotFound("Month not found")
    redirect_challenge = months[month - 1]
    redirect_path = reverse('monthly-challenge', args=[redirect_challenge])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge = monthly_challeneges[month]
        return render(request, "challenges/challenge.html", {"text":challenge, "month": month})
    except:
        return HttpResponseNotFound("<h1>Page not found</h1>")
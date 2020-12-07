from django.shortcuts import render
import random
import string


# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def mypassword_info(request):

    chart = list(string.ascii_lowercase)

    upper = request.GET.get("uppercase")
    special = request.GET.get('special')
    numbers = request.GET.get("numbers")
    if upper:
        chart.extend(string.ascii_uppercase)
    if special:
        chart.extend("@#$%^&*()?")
    if numbers:
        chart.extend(string.digits)
    lenght = int(request.GET.get('lenght'))

    samepassword = ""
    for x in range(lenght):
        samepassword += random.choice(chart)

    return render(request, 'password.html', {'viewpassword': samepassword})

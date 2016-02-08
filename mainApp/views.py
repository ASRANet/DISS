# -*- coding: UTF-8 -*-

from django.shortcuts import render
from mainApp.models import InfoPage, Item


def index(request):

    story_list = Item.objects.filter(page__name="index").order_by('order')

    return render(request, 'index.html', {"story_list": story_list})


def venue(request):
    return render(request, 'venue.html', {"story_list": Item.objects.filter(page__name="venue")})


def accomodation(request):
    return render(request, 'accomodation.html')


def contactus(request):
    return render(request, 'contactUs.html')


def travel(request):
    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": Item.objects.filter(page__name="index")})


def cookies(request):
    return render(request, 'cookies.html')

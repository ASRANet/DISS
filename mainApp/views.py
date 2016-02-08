# -*- coding: UTF-8 -*-

from django.shortcuts import render
from mainApp.models import InfoPage, Item


def index(request):

    story_list = Item.objects.filter(page__name="index").order_by('order')

    return render(request, 'index.html', {"story_list": story_list})


def venue(request):
    story_list = Item.objects.filter(page__name="venue").order_by('order')
    return render(request, 'venue.html', {"story_list": story_list})


def accomodation(request):
    story_list = Item.objects.filter(page__name="accomodation").order_by('order')
    return render(request, 'accomodation.html', {"story_list": story_list})


def contactus(request):
    return render(request, 'contactUs.html')


def travel(request):
    story_list = Item.objects.filter(page__name="travel").order_by('order')
    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": story_list})


def cookies(request):
    return render(request, 'cookies.html')

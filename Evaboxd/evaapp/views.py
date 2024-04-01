from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Show, Episode


class IndexViews(generic.ListView):
    template_name = 'evaapp/index.html'
    context_object_name = 'shows_list'

    def get_queryset(self):
        return Show.objects.order_by("-show_date")


class DetailViews(generic.DetailView):
    model = Show
    template_name = 'evaapp/show_details.html'
    # context_object_name = 'episode_list'
    #
    # def get_queryset(self):
    #     return Episode

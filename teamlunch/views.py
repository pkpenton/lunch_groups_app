# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

from teamlunch.forms import TeamLunchForm
from teamlunch.lunch_group_processor import (
    clean_lists,
    randomize_team,
    split_into_groups,
)


class TeamLunchView(View):

    def get(self, request):
        lunch_form = TeamLunchForm()

        return render(request, "teamlunch.html", {'lunch_form': lunch_form})

    def post(self, request):
        lunch_form = TeamLunchForm(request.POST)

        if lunch_form.is_valid():
            primary_team = lunch_form.cleaned_data.get('primary_team')
            guest_team = lunch_form.cleaned_data.get('guest_team')

            primary_team_split = (primary_team.split('\r\n'))
            guest_team_split = (guest_team.split('\r\n'))

            randomized_primary_team = randomize_team(clean_lists(primary_team_split))
            randomized_guest_team = randomize_team(clean_lists(guest_team_split))

            final_groups = split_into_groups(randomized_primary_team, randomized_guest_team)

            return render(request, 'lunchresults.html', {
                'final_groups': final_groups,
            })

        else:
            return render(request, "teamlunch.html", {'lunch_form': lunch_form})

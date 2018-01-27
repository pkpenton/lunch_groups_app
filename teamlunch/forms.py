from django import forms


class TeamLunchForm(forms.Form):
    primary_team = forms.CharField(label="Research Team:", max_length=10000, widget=forms.Textarea)
    guest_team = forms.CharField(label="Guest Team:", max_length=10000, widget=forms.Textarea)

from django import forms
from .models import UserProfile
from .models import Link
from .models import Vote

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank_score")

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote

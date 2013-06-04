from django.views.generic import ListView, DetailView
from .models import Link, UserProfile
from .forms import UserProfileForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 5


class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={"slug": self.request.user})

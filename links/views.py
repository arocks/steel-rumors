from django.views.generic import ListView
from .models import Link, Vote

class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 5

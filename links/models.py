from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class LinkVoteCountManager(models.Manager):
    def get_query_set(self):
        return super(LinkVoteCountManager, self).get_query_set().annotate(
            votes=Count('vote')).order_by("-votes")


class Link(models.Model):
    title = models.CharField("Headline", max_length=100)
    submitter = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)
    url = models.URLField("URL", max_length=250, blank=True)
    description = models.TextField(blank=True)

    with_votes = LinkVoteCountManager()
    objects = models.Manager()            # default manager

    def __unicode__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User)
    link = models.ForeignKey(Link)

    def __unicode__(self):
        return "%s voted %s" % (self.voter.username, self.link.title)

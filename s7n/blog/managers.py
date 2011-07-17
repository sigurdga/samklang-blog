from django.db.models import Manager
from django.db.models.query_utils import Q

from datetime import datetime

class LiveEntryManager(Manager):
    """Manager that returns posts which is set to be shown live"""

    def get_query_set(self):
        now = datetime.now
        return super(LiveEntryManager, self).get_query_set().filter(pub_date__lt=now).filter(
                Q(pub_enddate=None) | Q(pub_enddate__gt=now))



    def for_user(self, user=None):
        if user and user.is_authenticated():
            return self.get_query_set().filter(Q(group=None) | Q(group__user=user))
        else:
            return self.get_query_set().filter(group=None)

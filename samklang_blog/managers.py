from django.db.models.query_utils import Q
from samklang_utils.managers import PermissionManager

from datetime import datetime

class LiveEntryManager(PermissionManager):
    """Manager that returns posts which is set to be shown live"""

    def get_query_set(self):
        now = datetime.now
        return super(LiveEntryManager, self).get_query_set().filter(pub_date__lt=now).filter(
                Q(pub_enddate=None) | Q(pub_enddate__gt=now))

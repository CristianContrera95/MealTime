from typing import Optional
from uuid import UUID

from django.db.models import Manager


class CommonManager(Manager):

    def load_by_id(self, uuid: UUID) -> Optional:
        return super().filter(id=uuid).first()
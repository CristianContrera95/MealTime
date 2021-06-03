from datetime import date
from typing import Optional

from .common import CommonManager


class OrderManager(CommonManager):

    def load_by_day(self, day: date) -> Optional:
        return super().filter(for_day=day).first()

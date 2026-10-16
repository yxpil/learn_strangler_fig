"""Strangler Fig: gradually replace a legacy system by routing traffic
from old to new, slice by slice, until the old system is fully strangled."""
import random


class LegacySystem:
    def handle(self, request):
        return {"backend": "legacy", "data": f"old-{request}"}


class NewSystem:
    def handle(self, request):
        return {"backend": "new", "data": f"new-{request}"}


class StranglerGateway:
    def __init__(self, new_traffic_ratio=0.0):
        self.legacy = LegacySystem()
        self.new = NewSystem()
        self.new_ratio = new_traffic_ratio  # 0.0 = all legacy, 1.0 = all new

    def set_ratio(self, ratio):
        self.new_ratio = max(0.0, min(1.0, ratio))

    def route(self, request):
        if random.random() < self.new_ratio:
            return self.new.handle(request)
        return self.legacy.handle(request)

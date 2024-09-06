from .models import PersonQueue
from .models import Queue


class Queue:
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO, LIFO]

    def __init__(self, strategy):
        if strategy not in self.STRATEGIES:
            raise TypeError
        self.strategy = strategy

    def add(self, value):
        if self.strategy == self.FIFO:
            PersonQueue.objects.create(value=value)

    def pop(self):
        if self.strategy == self.FIFO:
            value = PersonQueue.objects.order_by("id").first()
            if value:
                value = value.value
                PersonQueue.objects.order_by("id").first().delete()
                return value
            return None


class UniqueQueue:
    LIFO = "LIFO"
    STRATEGIES = [LIFO]

    def __init__(self, strategy):
        if strategy not in self.STRATEGIES:
            raise TypeError
        self.strategy = strategy
        self.queue = []

    def add(self, item):
        if item not in self.queue:
            self.queue.append(item)

    def len_queue(self):
        return len(self.queue)

    def last_item_in_queue(self):
        if self.queue:
            return self.queue[-1]
        return None

    def pop(self):
        if self.queue:
            return self.queue.pop(-1)
        return None


# class UniqueQueue:
#     LIFO = "LIFO"
#     STRATEGIES = [LIFO]
#
#     def __init__(self, strategy):
#         if strategy not in self.STRATEGIES:
#             raise TypeError
#         self.strategy = strategy
#         self.queue = Queue.objects.all()
#
#     def add(self, item):
#         if not Queue.objects.filter(queue=item).exists():
#             Queue.objects.create(queue=item)
#
#     def len_queue(self):
#         return Queue.objects.count()
#
#     def last_item_in_queue(self):
#         if self.queue.exists():
#             last_queue_object = self.queue.last()
#             return last_queue_object.queue
#         return None
#
#     def pop(self):
#         queue = Queue.objects.order_by("id").last()
#         if queue:
#             queue = queue.queue
#             Queue.objects.order_by("id").last().delete()
#             return queue
#         return None

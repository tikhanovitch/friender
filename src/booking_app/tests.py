from django.test import TestCase
import unittest
from .queue import Queue
from .queue import UniqueQueue
import random

# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('FOO'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()
#_____________________________________________________________

#
# class TestQueue(TestCase):
#     def test_queue_exist(self):
#         q = Queue(strategy="FIFO")
#
#     def test_exist_strategy_fifo_and_lifo(self):
#         with self.assertRaises(TypeError):
#             q = Queue(strategy="LFA")
#
#     def test_add_some_value_to_queue(self):
#         q = Queue(strategy="FIFO")
#         first_value = 4
#         q.add(first_value)
#         get_value = q.pop()
#         self.assertEqual(get_value, first_value)
#
#     def test_add_queue_multi_value(self):
#         q = Queue(strategy="FIFO")
#         test_values = [4, 3, 2]
#         for ind in range(len(test_values)):
#             q.add(test_values[ind])
#
#         for ind in range(len(test_values)):
#             get_value = q.pop()
#             self.assertEqual(get_value, test_values[ind])
#
#     def test_add_value_mega_values(self):
#         q = Queue(strategy="FIFO")
#         first_value = 44
#         q.add(first_value)
#         for i in range(20):
#             value = random.randint(1, 10)
#             q.add(value)
#
#         get_value = q.pop()
#         self.assertEqual(get_value, first_value)
#
#     def test_empty_get_value_storage(self):
#         q = Queue(strategy="FIFO")
#         first_value = 44
#         q.add(first_value)
#         get_value = q.pop()
#         self.assertEqual(get_value, first_value)
#         get_value = q.pop()
#         self.assertIsNone(get_value)
#_____________________________________________________________


class TestUniqueQueue(TestCase):
    def test_unique_queue_exist(self):
        queue = UniqueQueue(strategy="LIFO")

    def test_exist_strategy_lifo(self):
        with self.assertRaises(TypeError):
            queue = UniqueQueue(strategy="FIFO")

    def test_add_some_item_to_queue(self):
        queue = UniqueQueue(strategy="LIFO")
        first_item = 25
        queue.add(first_item)
        get_item = queue.pop()
        self.assertEqual(get_item, first_item)

    def test_add_many_item_to_unique_queue(self):
        queue = UniqueQueue(strategy="LIFO")
        test_values = [1, 2, 3]
        for ind in range(len(test_values)):
            queue.add(test_values[ind])

        for ind in range(len(test_values)-1, -1):
            get_value = queue.pop()
            self.assertEqual(get_value, test_values[ind])

    def test_add_duplicate_items(self):
        queue = UniqueQueue(strategy="LIFO")
        first_item = 25
        second_item = 25
        queue.add(first_item)
        queue.add(second_item)
        test_len = 1
        self.assertEqual(queue.len_queue(), test_len)
        self.assertEqual(queue.last_item_in_queue(), first_item)

    def test_add_unique_items(self):
        queue = UniqueQueue(strategy="LIFO")
        first_item = 24
        second_item = 25
        test_len = 2
        queue.add(first_item)
        queue.add(second_item)
        self.assertEqual(queue.len_queue(), test_len)
        self.assertEqual(queue.last_item_in_queue(), second_item)

    def test_pop_lifo_strategy(self):
        queue = UniqueQueue(strategy="LIFO")
        first_item = 24
        second_item = 25
        test_len = 1
        queue.add(first_item)
        queue.add(second_item)
        popped_item = queue.pop()
        self.assertEqual(popped_item, second_item)
        self.assertEqual(queue.len_queue(), test_len)
        self.assertEqual(queue.last_item_in_queue(), first_item)

    def test_empty_queue_pop(self):
        queue = UniqueQueue(strategy="LIFO")
        queue.pop()
        self.assertIsNone(queue.last_item_in_queue())

    def test_last_item_in_queue_where_last_item_null(self):
        queue = UniqueQueue(strategy="LIFO")
        self.assertIsNone(queue.last_item_in_queue())

    def test_len_queue_without_items(self):
        queue = UniqueQueue(strategy="LIFO")
        test_len = 0
        self.assertEqual(queue.len_queue(), test_len)



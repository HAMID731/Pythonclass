import unittest
from Queue import PersonalQueue  # Assuming your custom class is in a file named personal_queue.py

class TestPersonalQueue(unittest.TestCase):

    def setUp(self):
        self.queue = PersonalQueue()

    def test_enqueue(self):
        self.queue.enqueue('a')
        self.assertEqual(self.queue.queue[-1], 'a')
        self.queue.enqueue('b')
        self.assertEqual(self.queue.queue[-1], 'b')

    def test_dequeue(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        item = self.queue.dequeue()
        self.assertEqual(item, 'a')
        self.assertEqual(self.queue.queue[0], 'b')

    def test_dequeue_empty(self):
        item = self.queue.dequeue()
        self.assertIsNone(item)

    def test_peek(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        item = self.queue.peek()
        self.assertEqual(item, 'a')

    def test_peek_empty(self):
        item = self.queue.peek()
        self.assertIsNone(item)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('a')
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.assertEqual(self.queue.size(), 2)

    def test_display(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.display()  

if __name__ == '__main__':
    unittest.main()

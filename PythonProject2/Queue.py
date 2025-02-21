class PersonalQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Added {item} to the queue.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Removed {item} from the queue.")
            return item
        else:
            print("The queue is empty, nothing to remove.")
            return None

    def peek(self):
        if not self.is_empty():
            print(f"Front of the queue: {self.queue[0]}")
            return self.queue[0]
        else:
            print("The queue is empty.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        print(f"Queue size: {len(self.queue)}")
        return len(self.queue)

    def display(self):
        print(f"Queue: {self.queue}")



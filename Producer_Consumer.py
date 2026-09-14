import random
import threading
import time

BUFFER_LIMIT = 5
TOTAL_ITEMS = 15

buffer = []
condition = threading.Condition()


def producer():
    for _ in range(TOTAL_ITEMS):
        item = random.randint(1, 100)

        with condition:
            while len(buffer) >= BUFFER_LIMIT:
                print("Buffer is full. Producer is waiting.")
                condition.wait()

            buffer.append(item)
            print(f"Produced {item}. Buffer: {buffer}")

            condition.notify()

        time.sleep(random.uniform(0.1, 1.0))


def consumer():
    for _ in range(TOTAL_ITEMS):
        with condition:
            while not buffer:
                print("Buffer is empty. Consumer is waiting.")
                condition.wait()

            item = buffer.pop(0)
            print(f"Consumed {item}. Buffer: {buffer}")

            condition.notify()

        time.sleep(random.uniform(0.3, 1.2))


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("All items were produced and consumed.")
